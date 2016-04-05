import ctypes

class t4py:
    libt4 = None
    dll_path = ''

    to_utf8 = False

    def __init__(self, dll_path):
        try:
            self.libt4=ctypes.WinDLL(dll_path)
        except:
            print "Open T4 DLL error!"

    def init_t4(self, sino_id, sino_pwd):
        init_t4=self.libt4.init_t4
        init_t4.argtypes = [ctypes.c_char_p]*3
        init_t4.restype = ctypes.c_char_p
        ret = init_t4(sino_id,sino_pwd,self.dll_path).decode('big5')
        if self.to_utf8: ret = ret.encode('utf8')
        return ret

    def show_version(self):
        show_version=self.libt4.show_version
        show_version.argtypes = []
        show_version.restype=ctypes.c_char_p
        ret = show_version().decode('big5')
        if self.to_utf8: ret = ret.encode('utf8')
        return ret

    def logout_t4(self):
        logout_t4=self.libt4.log_out
        logout_t4.argtypes = []
        logout_t4.restype = ctypes.c_int
        ret=logout_t4()
        if ret:    print "LOGOUT ERROR"
        return ret

    def show_list(self):
        show_list=self.libt4.show_list
        show_list.restype = ctypes.c_char_p
        ret = show_list()
        ret = ret.decode('big5').encode('utf8')
        return ret

    def get_fo_branch_account(self):
        branch=None
        account=None
        results=self.show_list()
        for i, result in enumerate(results.split('\n')):
            s=result.split('-')
            if len(s[0])==7:
                branch=s[0]
                account=s[1]
        return branch, account

    def get_stock_branch_account(self):
        branch=None
        account=None
        results=self.show_list()
        for i, result in enumerate(results.split('\n')):
            s=result.split('-')
            if len(s[0])==4:
                branch=s[0]
                account=s[1]
        return branch, account

    def get_response_log(self):
        get_response_log=self.libt4.get_response_log
        get_response_log.restype = ctypes.c_char_p
        ret = get_response_log().decode('big5')
        if self.to_utf8: ret = ret.encode('utf8')
        return ret


    def stock_balance_sum(self):
        stock_balance_sum=self.libt4.stock_balance_sum
        stock_balance_sum.restype = ctypes.c_char_p
        stock_balance_sum.argtypes = [ctypes.c_char_p]*4

        stock_balance_sum_type   = ctypes.c_char_p('A')
        stock_balance_sum_action = ctypes.c_char_p('0')

        branch, account = self.get_stock_branch_account()
        stock_balance_sum_branch  = ctypes.c_char_p(branch)
        stock_balance_sum_account = ctypes.c_char_p(account)

        ret = stock_balance_sum(branch, account, stock_balance_sum_type, stock_balance_sum_action).decode('big5')
        if self.to_utf8: ret = ret.encode('utf8')
        return ret


    def fo_unsettled_qry(self):
        fo_unsettled_qry=self.libt4.fo_unsettled_qry
        fo_unsettled_qry.restype = ctypes.c_char_p
        fo_unsettled_qry.argtypes = [ctypes.c_char_p]*11

        fo_unsettled_qry_flag    = ctypes.c_char_p('0000')
        fo_unsettled_qry_leng    = ctypes.c_char_p('0004')
        fo_unsettled_qry_next    = ctypes.c_char_p('0000')
        fo_unsettled_qry_prev    = ctypes.c_char_p('0000')
        fo_unsettled_qry_gubn    = ctypes.c_char_p('0')
        fo_unsettled_qry_grpname = ctypes.c_char_p('')
        fo_unsettled_qry_type1   = ctypes.c_char_p('0')
        fo_unsettled_qry_type2   = ctypes.c_char_p('0')
        fo_unsettled_qry_timeout = ctypes.c_char_p('1')

        branch, account = self.get_fo_branch_account()
        fo_unsettled_qry_branch  = ctypes.c_char_p(branch)
        fo_unsettled_qry_account = ctypes.c_char_p(account)

        ret =  fo_unsettled_qry(
                    fo_unsettled_qry_flag,   fo_unsettled_qry_leng,    fo_unsettled_qry_next,
                    fo_unsettled_qry_prev,   fo_unsettled_qry_gubn,    fo_unsettled_qry_grpname,
                    fo_unsettled_qry_branch, fo_unsettled_qry_account, fo_unsettled_qry_type1,
                    fo_unsettled_qry_type2,  fo_unsettled_qry_timeout)

        ret = ret.decode('big5')
        if self.to_utf8: ret = ret.encode('utf8')
        return ret
