class AliPay:

    def pay(self):
        print('通过支付宝消费')


class WeChatPay:

    def pay(self):
        print('通过微信消费')


class YinLianPay:

    def pays(self):
        print('通过银联消费')


class Order(object):

    def account(self, pay_obj):
        pay_obj.pay()


order = Order()

a = AliPay()
w = WeChatPay()
yl = YinLianPay()

order.account(a)
order.account(w)
# order.account(yl)
