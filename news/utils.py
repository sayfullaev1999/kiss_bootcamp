from uuid import UUID


def is_valid_status(status):
    return status in ['active', 'not_active']


def is_valid_uuid4(uuid):
    try:
        uuid_version = UUID(uuid).version
    except ValueError:
        return False
    return uuid_version == 4
