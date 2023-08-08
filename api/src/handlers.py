from api.src.proccess import CreateAccount,UpdateAccount,ConsultAccount



class AccountsHandler:
    @staticmethod
    def create_account(name,value):
        return CreateAccount().create_account(name,value)

    @staticmethod
    def update_value_account(account,value):
            return UpdateAccount().update_value_account(account,value)

    @staticmethod
    def consult_account(account):
            return ConsultAccount().consult_account(account)
    # @staticmethod
    # def get_category(category_id: int):
    #     return CategoriesProcess().get_category(category_id)

    # @staticmethod
    # def get_photos(
    #         category_id: int,
    #         current_page: int,
    #         items_per_page: int,
    #         order_by: str
    # ):
    #     return PhotosProcess().get_photos(
    #         category_id=category_id,
    #         current_page=current_page,
    #         items_per_page=items_per_page,
    #         order_by=order_by
    #     )

    # @staticmethod
    # def get_photo(
    #         photo_id: int,
    # ):
    #     return PhotosProcess().get_photo(
    #         photo_id=photo_id
    #     )

    # @staticmethod
    # def like_dislike_photo(photo_id: int, action: str):
    #     return PhotosProcess().like_dislike_photo(
    #         photo_id=photo_id,
    #         action=action
    #     )
