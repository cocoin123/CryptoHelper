from aiocryptopay import AioCryptoPay, Networks
import sys

class CryptoHelper():
    def __init__(self, token, network):
        self.token = token
        self.network = network

        if network == 'MAIN':
            self.network = Networks.MAIN_NET
        elif network == "TEST":
            self.network = Networks.TEST_NET

    async def check_balance(self):
        """
        Просмотр баланса на вашем CryptoPay кошельке.
        """
        try:
            crypto = AioCryptoPay(self.token, self.network) # Instantiate directly
            balance = await crypto.get_balance() # Call methods directly
            return balance  
        finally: 
            await crypto.close()
    async def transfer(
            self,
            user_id: int,
            amount: float,
            asset: str = 'USDT',
            fiat: str = None,
            currency_type: str = 'crypto'
    ): 
        """
        Перевод средств с одного пользователя на другого.\n

        Строка user_id: user_id человека которому хотите перевести деньги.\n
        Строка amount: сколько вы хотите перевести.\n
        Строка asset: валюта перевода. По умолчанию USDT.\n
        Строка fiat: сам хз).\n
        Строка currency_type: 'crypto' или 'fiat'.
        """
        try:
            crypto = AioCryptoPay(self.token, self.network) # Instantiate directly
            await crypto.transfer(
                user_id=user_id,
                amount=amount,
                asset=asset,
                fiat=fiat,
                currency_type=currency_type
            )
        finally:
            await crypto.close()
        
        async def create_check(
                self, 
                asset: str = 'USDT', 
                amount: float = None,
                description: str = None,
                hidden_message: str = None,
                paid_btn_name: str = None,
                paid_btn_url: str = None,
        ):
            """
            Создание чека.

            asset: Криптовалюта для создание чека. По умолчанию USDT.\n
            amount: Сумма чека. По умолчанию None.\n
            description: Описание чека. По умолчанию None.\n
            hidden_message: Скрытое сообщение. По умолчанию None.
            """
            try:
                crypto = AioCryptoPay(self.token, self.network) # Instantiate directly

                check = await crypto.create_check(
                    asset=asset,
                    amount=amount,
                    description=description,
                    hidden_message=hidden_message,
                    paid_btn_name=paid_btn_name,
                    paid_btn_url=paid_btn_url
                )
                return check.bot_invoice_url
            finally:
                await crypto.close()
    async def delete_check(
            self,
            check_id: int
    ):
        """
        check_id: можно узнать через метод get_checks().
        """
        try:
            crypto = AioCryptoPay(self.token, self.network) # Instantiate directly

            await crypto.delete_check(check_id)
        finally:
            await crypto.close()
    async def get_checks(
            self,
    ):
        """
        Информация про чеки.
        """
        try:
            crypto = AioCryptoPay(self.token, self.network) # Instantiate directly

            checks = await crypto.get_checks()
            return checks
        finally:
            await crypto.close()
    async def get_invoices(
            self,
    ):
        """
        Информация про счета.
        """
        crypto = AioCryptoPay(self.token, self.network) # Instantiate directly
        invoices = await crypto.get_invoices()
        return invoices
        
    async def create_invoice(
            self,
            amount: float,
            asset: str = 'USDT',
            description: str = None,
    ):
        """
        Созданиче счета\n

        amount: сумма счета.\n
        asset: валюта счета. По умолчанию USDT.\n
        description: описание счета. По умолчанию None.\n
        """
        try:
            crypto = AioCryptoPay(self.token, self.network) # Instantiate directly

            invoice = await crypto.create_invoice(
                amount=amount,
                asset=asset,
                description=description
            )
            return invoice.bot_invoice_url
        finally:
            await crypto.close()
    async def get_invoice_status(
            self,
            invoice_id: int
    ):
        """
        Узнать статус счета.\n

        invoice_id: можно узнать через метод get_invoices().
        """
        try:
            crypto = AioCryptoPay(self.token, self.network) # Instantiate directly

            status = await crypto.get_invoice(invoice_id)
            return status.status
        finally:
            await crypto.close()
