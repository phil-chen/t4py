# -*- coding: utf-8 -*-

import unittest
import t4py

t4_dll_path = 'c:/T4/t4.dll'
account = ''
passwd = ''

class Test_t4py(unittest.TestCase):
    def test_1_load_dll(self):
        self.assertTrue(isinstance(t4,t4py.t4py))

    def test_2_init_t4(self):
        ret=t4.init_t4(account,passwd)
        print ret

    def test_3_show_version(self):
        ret=t4.show_version()
        print ret

    def test_4_fo_unsettled_qry(self):
        ret = t4.fo_unsettled_qry()
        print ret

    def test_5_stock_balance_sum(self):
        ret = t4.stock_balance_sum()
        print ret

    def test_6_get_response_log(self):
        ret=t4.get_response_log()
        print ret

    def test_99_logout_t4(self):
        ret=t4.logout_t4()
        self.assertEqual(ret, 0)




if __name__ == '__main__':
    t4 = t4py.t4py(t4_dll_path)

    unittest.TestLoader.sortTestMethodsUsing = None
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_t4py)
    unittest.TextTestRunner(verbosity=2).run(suite)
