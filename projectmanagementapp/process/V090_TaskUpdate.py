"""
ビュークラス
V120_userKoshn
質問作成ページ用View
エラーフラグ：0(正常終了),1(業務エラー),2(システムエラー)
flg_return：0(render),1(redirect)

flg_return==0の時、「template」「context」必須
flg_return==1の時、「path_name」必須

"""

import datetime
from django.urls import reverse
from . import (C010_Const,C030_MessageUtil,C050_StringUtil,
                S110_UpdateTask,
)

def main(request,urlID,seq):
    #--View共通----------------------------------------------
    #戻り値用の変数宣言
    flg_return = ""
    template = ''
    context = {}
    path_name = ''
    #-------------------------------------------------------
    try:
        if request.method == 'POST':
            #POSTの場合
            """
            POST時の処理を書く。
            パターンに応じてflg_returnの値を設定する。
            bottunパターンによって処理を分けたりもするかも。
            例は、redirect
            """
            errflg = "0"
            #更新ボタンの場合
            #サービスのパラメータをリクエストから取得する--------------------------------------
            projectID = request.session['projectID']
            taskTitle = request.POST['taskTitle']
            taskTant = request.POST['taskTant']
            kignDate = request.POST['kignDate']
            taskStatus = request.POST['taskStatus']
            taskDetail = request.POST['taskDetail']
            taskNaiyo = request.POST['taskNaiyo']
            updUserID = "SYSTEM000000000000"
            #loginKbn =  "0"
            #サービスのパラメータをリクエストから取得する--------------------------------------
            #==チェック処理=============================================================================================
            #チェック処理
            #単項目チェック-------------------------------------------------------------------------------------------------
            itemName_taskName = "タスク名"
            itemName_kignDate = "期限日"
            #タスク名
            if C050_StringUtil.isAllSpace(taskTitle):
                errflg = "1"
                C030_MessageUtil.setMessage(request,"E0001",(itemName_taskName,))
            if C050_StringUtil.isAllSpace(kignDate):
                errflg = "1"
                C030_MessageUtil.setMessage(request,"E0001",(itemName_kignDate,))
            #単項目チェック-------------------------------------------------------------------------------------------------
            #チェックNGの場合、処理を終了して再描画
            if errflg == "1":
                flg_return = "0"
                template = 'projectmanagementapp/T080_TaskDetail.html'
                
                json_taskInfo_S130 = {"SEQ":seq,
                                        "TASKTITLE":taskTitle,
                                        "TANTSH":taskTant,
                                        "KIHYO_DATE":kignDate,
                                        "TASKSTATUS":taskStatus,
                                        "TASKDETAIL":taskDetail,
                                        "NAIYO":taskNaiyo,
                                        }

                context = {**context,**{"json_taskInfo_S130":json_taskInfo_S130}}
                #戻り値用のjsonを作成
                json_view = {'flg_return':flg_return, 'template':template, 'context':context, 'path_name':path_name}
                return json_view

            #==チェック処理=============================================================================================

            #--S110-------------------------------------------------------------------------
            json_S110 = S110_UpdateTask.main(projectID,seq,taskTitle,taskDetail,taskNaiyo,taskTant,None,kignDate,taskStatus,updUserID)
            #個々の値を取得
            flg_S110 = json_S110["json_CommonInfo"]["errflg"]
            list_msgInfo_S110 = json_S110["json_CommonInfo"]["list_msgInfo"]
            #str_userID_S160 = json_S110["str_userID"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S110)
            #-------------------------------------------------------------------------------
            flg_return = "1"
            path_name = 'projectmanagementapp:taskDetail'
        else:
            #POST以外の場合
            """
            POST以外時の処理を書く。
            パターンに応じてflg_returnの値を設定する。
            bottunパターンによって処理を分けたりもするかも。
            例は、render
            """
        
        #戻り値用のjsonを作成
        json_view = {'flg_return':flg_return, 'template':template, 'context':context, 'path_name':path_name}
        return json_view
    #==例外処理==========================================================================================
    except Exception as e :
        #システムエラー共通処理
        C030_MessageUtil.systemErrorCommonMethod()
        raise
    #====================================================================================================

