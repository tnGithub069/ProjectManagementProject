"""
共通クラス
C010_Const
共通的な定数を格納する

"""
from django.contrib.messages import constants
import MySQLdb


#Djangoメッセージレベル
DEBUG = constants.DEBUG
INFO = constants.INFO
SUCCESS = constants.SUCCESS
WARNING = constants.WARNING
ERROR = constants.ERROR

#シーケンステーブルID
S010 = {"tableID":"S010_USER_ID","header":"U"}
S100 = {"tableID":"S100_PROJECT_ID","header":"P"}

#共通画面パス
PATH_NAME_ERR = 'projectmanagementapp:systemError'
PATH_NAME_SUCCESS = 'projectmanagementapp:success'
PATH_NAME_V070 = "'projectmanagementapp:projectTop' urlID"
