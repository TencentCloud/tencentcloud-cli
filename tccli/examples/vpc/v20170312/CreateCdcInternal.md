**Example 1: 创建cdc实体**



Input: 

```
tccli vpc CreateCdcInternal --cli-unfold-argument  \
    --CdcRequestSet.0.Owner 123456 \
    --CdcRequestSet.0.UniqCdcSiteId vpc-xxxxxxxx \
    --CdcRequestSet.0.UniqCdcId 10.0.0.0 \
    --CdcRequestSet.0.NetType 2 \
    --CdcRequestSet.0.ZoneId 16 \
    --CdcRequestSet.0.Description desc \
    --CdcRequestSet.0.DataPlaneVpngwBandwidth 100 \
    --CdcRequestSet.0.CdcDataPlaneVpngwBandwidth 100 \
    --CdcRequestSet.0.ControlVpngwBandwidth 100 \
    --CdcRequestSet.0.OobVpngwBandwidth 100 \
    --CdcRequestSet.0.CdcIdcVip 10.0.0.0 \
    --CdcRequestSet.0.CdcDcVip 10.0.0.0 \
    --CdcRequestSet.0.CdcLocalWanVip 10.0.0.0 \
    --CdcRequestSet.0.CdcLocalWanSnatCidr 10.0.0.0 \
    --CdcRequestSet.0.CdcVpngwVlan 3 \
    --CdcRequestSet.0.CdcNormalVlan 4 \
    --CdcRequestSet.0.CdcVpngwConnConf ssss \
    --CdcRequestSet.0.CdcNormalConnConf ssss \
    --CdcRequestSet.0.CdcControlVpngwVip 10.0.0.0 \
    --CdcRequestSet.0.CdcOobVpngwVip 10.0.0.0 \
    --CdcRequestSet.0.CdcControlCidr 10.0.0.0 \
    --CdcRequestSet.0.CdcOobCidr 10.0.0.0 \
    --CdcRequestSet.0.CdcControlVpngwAddress 10.0.0.0 \
    --CdcRequestSet.0.CdcOobVpngwAddress 10.0.0.0 \
    --CdcRequestSet.0.CdcP4gwAddress 10.0.0.0 \
    --CdcRequestSet.0.CdcHostAddress 10.0.0.0
```

Output: 
```
{
    "Response": {
        "CdcSet": [
            {
                "OobVpngwBandwidth": 1000,
                "ControlVpngwBandwidth": 1000,
                "Description": "",
                "OobVpcId": 80566,
                "UniqueCdcId": "cdc-aisoqjsi",
                "ProxyGroup": [
                    {},
                    {}
                ],
                "ZoneId": 800005,
                "UniqCdcSiteId": "cdcsite-8e0ypm3z",
                "UniqControlVpcId": "vpc-obqs41yl",
                "CdcId": 81,
                "NetType": 0,
                "Owner": "251197522",
                "UniqOobVpcId": "vpc-2uiynkpt",
                "ControlVpcId": 80505,
                "CreateTime": "0000-00-00 00:00:00"
            }
        ],
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

