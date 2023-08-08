from api.src.querysets import Queryset
from api.src.models import Account
import random
class CreateAccount:
    @staticmethod
    def create_account(name,value):

        account_number = int(''.join(random.sample('0123456789', 8)))
        account = Account(name,value)
        qs = Queryset()
        while(qs.validate_account(account_number)):
            account_number = int(''.join(random.sample('0123456789', 8)))

        account.account = account_number
        qs = Queryset()
        res = qs.create_account(account)
        return {
            "status": 200,
            "data": res
        }

    @staticmethod
    def get_category(category_id: int):
        qs = Queryset()
        res = qs.get_category(category_id)
        return {
            "status": 200,
            "data": res
        }

class UpdateAccount:
    @staticmethod
    def update_value_account(account,value):
        qs = Queryset()
        return qs.update_value_account(account, value)

class ConsultAccount:
    @staticmethod
    def consult_account(account: int):
        qs = Queryset()
        return qs.consult_account(account)





class PhotosProcess:
    @staticmethod
    def get_photos(
            category_id: int,
            current_page: int,
            items_per_page: int,
            order_by: str
    ):
        qs = Queryset()
        return qs.get_all_photos(
            category_id,
            current_page,
            items_per_page,
            order_by
        )

    @staticmethod
    def get_photo(
            photo_id: int,
    ):
        qs = Queryset()
        return qs.get_photo(
            photo_id,
        )

    @staticmethod
    def like_dislike_photo(photo_id: int, action: str):
        qs = Queryset()
        return qs.like_dislike_photo(photo_id, action)
