import ipaddress
import random
import struct


class TLV:
    M_SOURCE_ADDRESS = 0
    M_MODE = 1
    M_TIMEOUT = 2
    M_CHALLENGE = 3
    M_RESPONSE = 4
    M_LINK_LAYER_FRAME_COUNTER = 5
    M_LINK_QUALITY = 6
    M_NETWORK_PARAMETER = 7
    M_MLE_FRAME_COUNTER = 8
    M_ROUTE64 = 9
    M_ADDRESS16 = 10
    M_LEADER_DATA = 11
    M_NETWORK_DATA = 12
    M_TLV_REQUEST = 13
    M_SCAN_MASK = 14
    M_CONNECTIVITY = 15
    M_LINK_MARGIN = 16
    M_STATUS = 17
    M_VERSION = 18
    M_ADDRESS_REGISTRATION = 19
    M_CHANNEL = 20
    M_PAN_ID = 21
    M_ACTIVE_TIMESTAMP = 22
    M_PENDING_TIMESTAMP = 23
    M_ACTIVE_OPERATIONAL_DATASET = 24
    M_PENDING_OPERATIONAL_DATASET = 25
    M_THREAD_DISCOVERY = 26
    M_CIM_DEVICE_INTERFACE_DATA = 27
    M_CIM_PROVISIONER_INTERFACE_DATA_ = 28
    M_CIM_PROVISIONING_DATASET = 29
    M_CIM_DISCOVERY_REQUEST = 30
    M_SECURE_DISSEMINATION = 32
    M_CSLCHANNEL = 80
    M_CSLMAXPERIOD = 81
    M_CSLAWAKEDURATION = 82
    M_CSLSNIFFDURATION = 83
    M_CSLMODE = 84
    M_CSLSYNCHRONIZEDTIMEOUTTLV = 85
    M_CSL_ACCURACY = 86
    M_LINK_METRICS_QUERY = 87
    L_LINK_METRICS_QUERY_ID = 1
    L_LINK_METRICS_QUERY_OPTIONS = 2
    M_LINK_METRICS_MANAGEMENT = 88
    L_FORWARD_PROBING_REGISTRATION = 3
    L_REVERSE_PROBING_REGISTRATION = 4
    L_LINK_METRICS_STATUS = 5
    L_SERIES_TRACKING_CAPABILITIES = 6
    L_ENHANCED_ACK_CONFIGURATION = 7
    M_LINK_METRICS_REPORT = 89
    L_LINK_METRIC_REPORT = 0
    M_PROBE = 90
    C_CHANNEL = 0
    C_PAN_ID = 1
    C_EXTENDED_PAN_ID = 2
    C_NETWORK_NAME = 3
    C_PSKC = 4
    C_NETWORK_MASTER_KEY = 5
    C_NETWORK_KEY_SEQUENCE_COUNTER = 6
    C_NETWORK_MESH_LOCAL_PREFIX = 7
    C_STEERING_DATA = 8
    C_BORDER_AGENT_LOCATOR = 9
    C_COMMISSIONER_ID = 10
    C_COMMISSIONER_SESSION_ID = 11
    C_SECURITY_POLICY = 12
    C_ACTIVE_TIMESTAMP = 14
    C_COMMISSIONER_UDP_PORT = 15
    C_PENDING_TIMESTAMP = 51
    C_DELAY_TIMER = 52
    C_CHANNEL_MASK = 53
    C_SECURE_DISSEMINATION = 58
    C_THREAD_DOMAIN_NAME = 59
    C_DOMAIN_PREFIX = 60
    C_AE_STEERING_DATA = 61
    C_NMKP_STEERING_DATA = 62
    C_COMMISSIONER_TOKEN = 63
    C_COMMISSIONER_SIGNATURE = 64
    C_AE_UDP_PORT = 65
    C_NMKP_UDP_PORT = 66
    C_TRI_HOSTNAME = 67
    C_REGISTRAR_IPV6_ADDRESS = 68
    C_REGISTRAR_HOSTNAME = 69
    C_GET = 13
    C_STATE = 16
    C_JOINER_DTLS_ENCAPSULATION = 17
    C_JOINER_UDP_PORT = 18
    C_JOINER_IID = 19
    C_JOINER_ROUTER_LOCATOR = 20
    C_JOINER_ROUTER_KEK = 21
    C_COUNT = 54
    C_PERIOD = 55
    C_SCAN_DURATION = 56
    C_ENERGY_LIST = 57
    C_PROVISIONING_URL = 32
    C_VENDOR_NAME = 33
    C_VENDOR_MODEL = 34
    C_VENDOR_SW_VERSION = 35
    C_VENDOR_DATA = 36
    C_VENDOR_STACK_VERSION = 37
    C_UDP_ENCAPSULATION = 48
    C_IPV6_ADDRESS = 49
    C_DISCOVERY_REQUEST = 128
    C_DISCOVERY_RESPONSE = 129
    C_ACTIVE_OPERATIONAL_DATASET = 130
    C_CIM_IDENTIFIER = 131
    C_CIM_PROVISIONING_DATASET_TIMESTAMP = 132
    C_CIM_PROVISIONING_CONFIGURATION_ID = 133
    C_CIM_PROVISIONING_DATASET_SOURCE = 134
    C_CIM_ANNOUNCE_TIMING = 135
    C_CIM_PREFIX_SET = 136
    C_CIM_DEVICE_INTERFACE_CONFIGURATION = 137
    C_CIM_PROVISIONER_CONFIGURATION_ = 138
    C_CIM_RX_OFF_WHEN_IDLE_CONFIGURATION = 139
    C_CIM_ADDRESS_SET = 140
    C_CIM_DEVICE_DISCOVERY_REQUEST = 141
    C_CIM_PROVISIONER_DISCOVERY_REQUEST = 142
    C_CIM_SECURITY_MATERIAL = 143
    N_HAS_ROUTE = 0
    N_PREFIX = 1
    N_BORDER_ROUTER = 2
    N_6LOWPAN_ID = 3
    N_COMMISSIONING_DATA = 4
    N_SERVICE = 5
    N_SERVER = 6
    A_TARGET_EID = 0
    A_MAC_EXTENDED_ADDRESS = 1
    A_RLOC16 = 2
    A_ML_EID = 3
    A_STATUS = 4
    A_TIME_SINCE_LAST_TRANSACTION = 6
    A_ROUTER_MASK = 7
    A_ND_OPTION = 8
    A_ND_DATA = 9
    A_THREAD_NETWORK_DATA = 10
    A_TIMEOUT = 11
    A_NETWORK_NAME = 12
    A_IPV6_ADDRESSES = 14
    A_COMMISSIONER_SESSION_ID = 15
    D_MAC_EXTENDED_ADDRESS = 0
    D_MAC_ADDRESS = 1
    D_MODE = 2
    D_TIMEOUT = 3
    D_CONNECTIVITY = 4
    D_ROUTE64 = 5
    D_LEADER_DATA = 6
    D_NETWORK_DATA = 7
    D_IPV6_ADRESS_LIST = 8
    D_MAC_COUNTERS = 9
    D_BATTERY_LEVEL = 14
    D_SUPPLY_VOLTAGE = 15
    D_CHILD_TABLE = 16
    D_CHANNEL_PAGES = 17
    D_TYPE_LIST = 18


class URI:
    D_DG = '/d/dg'
    C_AG = '/c/ag'
    N_MR = '/n/mr'
    N_DR = '/n/dr'
    B_BMR = '/b/bmr'
    B_BQ = '/b/bq'
    B_BA = '/b/ba'
    A_AQ = '/a/aq'
    A_AN = '/a/an'
    A_AE = '/a/ae'

    @staticmethod
    def tuple(uri):
        splitted = uri.split('/')
        return (splitted[1], splitted[2])


class DEFS:
    PORT_COAP = 5683
    PORT_MC = 49191
    PORT_MM = 61631
    PORT_BB = PORT_MM
    MIN_MLR_TIMEOUT = 300
    DUA_DAD_QUERY_TIMEOUT = 1
    DUA_DAD_REPEAT = 3
    DUA_RECENT_TIME = 20
    BBR_SEQ = random.randint(0, 255)
    THREAD_ENTERPRISE_NUMBER = 44970
    THREAD_SERVICE_DATA_BBR = '01'
    THREAD_SERVICE_DATA_FMT = '!BHI'
    MAX_NEIGHBOR_ADVERTISEMENT = 3
    RETRANS_TIMER = 1

    # Not defined by Thread
    BBR_DEF_REREG_DELAY = 6
    BBR_DEF_MLR_TIMEOUT = 3600


def get_prefix_based_mcast(prefix, groupid):
    '''RFC 3306'''
    prefix = prefix.split('/')[0]
    prefix_bytes = ipaddress.IPv6Address(prefix).packed
    maddr_bytes = (
        bytes.fromhex('ff320040') + prefix_bytes[0:8] + struct.pack('>I', groupid)
    )
    return ipaddress.IPv6Address(maddr_bytes).compressed


def get_rloc_from_short(prefix, rloc16):
    prefix = prefix.split('/')[0]
    prefix_bytes = ipaddress.IPv6Address(prefix).packed
    rloc_bytes = prefix_bytes[0:8] + bytes.fromhex('000000fffe00' + rloc16)
    return ipaddress.IPv6Address(rloc_bytes).compressed
