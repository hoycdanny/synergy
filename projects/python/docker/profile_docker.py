import sys
import importlib

SRVR_HWARE_URI = sys.modules['__main__'].SRVR_HWARE_URI
SRVR_HWARE_TYPE_URI = sys.modules['__main__'].SRVR_HWARE_TYPE_URI
ENCL_GROUP_URI = sys.modules['__main__'].ENCL_GROUP_URI
DEPL_NET_URI = sys.modules['__main__'].DEPL_NET_URI
DEPL_PLAN_URI = sys.modules['__main__'].DEPL_PLAN_URI
NET_URI = sys.modules['__main__'].NET_URI

config_module = sys.modules['__main__'].config_module
config = importlib.import_module(config_module)

profile_def = {
    "type": "ServerProfileV6",
    "serverHardwareUri": SRVR_HWARE_URI,
    "serverHardwareTypeUri": SRVR_HWARE_TYPE_URI,
    "enclosureGroupUri": ENCL_GROUP_URI,
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": config.PROFILE_NAME,
    "description": "",
    "affinity": "Bay",
    "connections": [
        {
            "id": 1,
            "name": "Deployment Network A",
            "functionType": "Ethernet",
            "portId": "Mezz 3:1",
            "requestedMbps": "2500",
            "networkUri": DEPL_NET_URI,
            "boot": {
                "priority": "Primary",
                "initiatorNameSource": "ProfileInitiatorName",
                "firstBootTargetIp": None,
                "secondBootTargetIp": "",
                "secondBootTargetPort": "",
                "initiatorName": None,
                "initiatorIp": None,
                "bootTargetName": None,
                "bootTargetLun": None
            },
            "mac": None,
            "wwpn": "",
            "wwnn": "",
            "requestedVFs": "Auto"
        },
        {
            "allocatedMbps": 10000,
            "allocatedVFs": 0,
            "boot": {
                "chapLevel": "None",
                "initiatorNameSource": "ProfileInitiatorName",
                "priority": "NotBootable"
            },
            "functionType": "Ethernet",
            "id": 2,
            "interconnectUri": "/rest/interconnects/f2206d00-123d-4bab-a801-4dada6d4f442",
            "macType": "Virtual",
            "maximumMbps": 10000,
            "name": "Ether-A",
            "networkUri": NET_URI,
            "portId": "Mezz 3:1",
            "requestedMbps": "10000",
            "requestedVFs": "0",
            "wwnn": "",
            "wwpn": "",
            "wwpnType": "Virtual"
        },
        {
            "allocatedMbps": 10000,
            "allocatedVFs": 0,
            "boot": {
                "chapLevel": "None",
                "initiatorNameSource": "ProfileInitiatorName",
                "priority": "NotBootable"
            },
            "functionType": "Ethernet",
            "id": 3,
            "interconnectUri": "/rest/interconnects/afc873c9-5069-4f9f-95db-7e6032cc54b9",
            "macType": "Virtual",
            "maximumMbps": 10000,
            "name": "Ether-B",
            "networkUri": NET_URI,
            "portId": "Mezz 3:2",
            "requestedMbps": "10000",
            "requestedVFs": "0",
            "wwnn": "",
            "wwpn": "",
            "wwpnType": "Virtual"
        }
    ],
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk"
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "Auto"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": []
    },
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": {
        "osCustomAttributes": [
            {
                "name": "SERVER_FQDN",
                "value": config.SERVER_FQDN
            },
            {
                "name": "CONSUL_FQDN",
                "value": config.CONSUL_FQDN
            },
            {
                "name": "DATADOG_TAG",
                "value": config.DATADOG_TAG
            },
            {
                "name": "VLAN_ID",
                "value": config.VLAN_ID
            }
        ],
        "osDeploymentPlanUri": DEPL_PLAN_URI,
        "osVolumeUri": ""
    },
    "localStorage": {
        "controllers": [],
        "sasLogicalJBODs": [
            {
                "deviceSlot": "Mezz 1",
                "driveMaxSizeGB": 2000,
                "driveMinSizeGB": 1000,
                "driveTechnology": "SasHdd",
                "id": 1,
                "name": "1TB_LVM_docker",
                "numPhysicalDrives": 1,
                "sasLogicalJBODUri": "",
            }
        ]
    },
    "sanStorage": None
}
