from collections import namedtuple
from ibanity import Ibanity


def get_list(financial_institution_id, sandbox_user_id, sandbox_account_id, params={}):
    uri = Ibanity.client.api_schema["sandbox"]["transactions"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{sandboxUserId}", sandbox_user_id) \
        .replace("{sandboxAccountId}", sandbox_account_id)\
        .replace("{sandboxTransactionId}", "")
    response = Ibanity.client.get(uri, params, None)
    return list(
        map(
            lambda transaction:
            __create_transaction_named_tuple__(transaction), response["data"]
        )
    )


def create(financial_institution_id, sandbox_user_id, sandbox_account_id, attributes):
    uri = Ibanity.client.api_schema["sandbox"]["transactions"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{sandboxUserId}", sandbox_user_id) \
        .replace("{sandboxAccountId}", sandbox_account_id)\
        .replace("{sandboxTransactionId}", "")
    body = {
        "data": {
            "type": "sandboxTransaction",
            "attributes": attributes
        }
    }
    response = Ibanity.client.post(uri, body, {}, None)
    return __create_transaction_named_tuple__(response["data"])


def delete(financial_institution_id, sandbox_user_id, sandbox_account_id, id):
    uri = Ibanity.client.api_schema["sandbox"]["transactions"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{sandboxUserId}", sandbox_user_id) \
        .replace("{sandboxAccountId}", sandbox_account_id)\
        .replace("{sandboxTransactionId}", id)
    response = Ibanity.client.delete(uri, {}, None)
    return __create_transaction_named_tuple__(response["data"])


def find(financial_institution_id, sandbox_user_id, sandbox_account_id, id):
    uri = Ibanity.client.api_schema["sandbox"]["transactions"] \
        .replace("{financialInstitutionId}", financial_institution_id) \
        .replace("{sandboxUserId}", sandbox_user_id) \
        .replace("{sandboxAccountId}", sandbox_account_id)\
        .replace("{sandboxTransactionId}", id)
    response = Ibanity.client.get(uri, {}, None)
    return __create_transaction_named_tuple__(response["data"])


def __create_transaction_named_tuple__(transaction):
    return namedtuple("SandboxTransaction", transaction.keys())(**transaction)
