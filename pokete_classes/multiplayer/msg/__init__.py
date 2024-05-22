import bs_rpc
from .version_mismatch import handle_version_mismatch
from .map_data import handle_map_data

TYPE_HANDSHAKE = "pokete.handshake"
TYPE_VERSION_MISMATCH = "pokete.error.version_mismatch"
TYPE_MAP_DATA = "pokete.map_data"
TYPE_USER_ALREADY_PRESENT = "pokete.error.user_already_present"


def get_registry():
    reg = bs_rpc.Registry()

    reg.register(TYPE_VERSION_MISMATCH, handle_version_mismatch)
    reg.register(TYPE_MAP_DATA, handle_map_data)
    reg.register(TYPE_USER_ALREADY_PRESENT, handle_map_data)

    return reg
