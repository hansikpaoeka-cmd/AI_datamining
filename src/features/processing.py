def show_application_detail(application,show_detail=False):
    '''
    :param application:申请数据
    :param show_detail: 是否显示详细数据
    :return:
    '''
    users = application['SK_ID_CURR'].nunique()
    default_users = len(application[application['TARGET']==1]['SK_ID_CURR'].unique())
    if show_detail:
        rows = application['SK_ID_CURR'].shape[0]
        print('#申请表中数据条目数:',rows)
        print('#申请表中申请用户数量:',users)
        print('#申请表中违约用户数量:',default_users)
        ratio = default_users/users
        print('的申请用户违约:%.2f%%'%(ratio*100))
    return users,default_users