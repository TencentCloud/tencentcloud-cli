**Example 1: 获取集群服务组信息**

获取集群服务组信息

Input: 

```
tccli emr DescribeServiceGroups --cli-unfold-argument  \
    --InstanceId emr-ikoyp9nw \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "444f91de-cbe0-4289-b022-16502d657be5",
        "ServiceGroupList": [
            {
                "AccessInfo": "",
                "AddTime": "2024-01-30 13:05:59",
                "ClusterId": 52446,
                "CmdServiceOpsInfo": null,
                "ExitInvalidParam": false,
                "IsExternal": false,
                "IsSupportDataMove": false,
                "IsSupportFederation": false,
                "IsSupportMonitor": false,
                "IsSupportReStart": false,
                "IsSupportServiceUpdate": false,
                "IsSupportSubmitConf": true,
                "IsSupportUninstall": false,
                "PathsInfo": "/usr/lib/sysctl.d",
                "ServiceConfStatusNumStatistic": {
                    "ExpiredConfNum": 0,
                    "FailedConfNum": 0
                },
                "ServiceDetectStatus": 0,
                "ServiceNodeList": [
                    {
                        "CoreDeploy": 3,
                        "CoreNecessary": 0,
                        "NodeName": "Sysctl",
                        "NodeType": 91,
                        "RestartPolicies": [
                            {
                                "BatchSizeRange": [
                                    1,
                                    99999
                                ],
                                "Describe": "默认重启模式",
                                "DisplayName": "默认重启模式",
                                "IsDefault": "true",
                                "Name": "default"
                            }
                        ],
                        "TaskDeploy": 0,
                        "TaskNecessary": 0
                    }
                ],
                "ServiceType": 43,
                "SoftName": "RUNTIME",
                "SoftVersion": "1.0.0",
                "Status": 0,
                "UserGroup": "root",
                "UserName": "root",
                "VAddress": "",
                "WebUiDetectStatus": 0,
                "WebUiUrl": "--"
            },
            {
                "AccessInfo": "Slapd IPC:172.27.16.21:389\n",
                "AddTime": "2024-01-30 13:05:59",
                "ClusterId": 52446,
                "CmdServiceOpsInfo": null,
                "ExitInvalidParam": false,
                "IsExternal": false,
                "IsSupportDataMove": false,
                "IsSupportFederation": false,
                "IsSupportMonitor": false,
                "IsSupportReStart": false,
                "IsSupportServiceUpdate": false,
                "IsSupportSubmitConf": false,
                "IsSupportUninstall": false,
                "PathsInfo": "/usr/libexec/openldap",
                "ServiceConfStatusNumStatistic": {
                    "ExpiredConfNum": 0,
                    "FailedConfNum": 0
                },
                "ServiceDetectStatus": 1,
                "ServiceNodeList": [
                    {
                        "CoreDeploy": 1,
                        "CoreNecessary": 0,
                        "NodeName": "slapd",
                        "NodeType": 51,
                        "RestartPolicies": [
                            {
                                "BatchSizeRange": [
                                    1,
                                    99999
                                ],
                                "Describe": "默认重启模式",
                                "DisplayName": "默认重启模式",
                                "IsDefault": "true",
                                "Name": "default"
                            }
                        ],
                        "TaskDeploy": 0,
                        "TaskNecessary": 0
                    }
                ],
                "ServiceType": 39,
                "SoftName": "OPENLDAP",
                "SoftVersion": "2.4.44",
                "Status": 0,
                "UserGroup": "root",
                "UserName": "root",
                "VAddress": "",
                "WebUiDetectStatus": 0,
                "WebUiUrl": "--"
            },
            {
                "AccessInfo": "QuorumPeerMain IPC:172.27.16.21:2181\n",
                "AddTime": "2024-01-30 13:05:59",
                "ClusterId": 52446,
                "CmdServiceOpsInfo": null,
                "ExitInvalidParam": false,
                "IsExternal": false,
                "IsSupportDataMove": false,
                "IsSupportFederation": false,
                "IsSupportMonitor": true,
                "IsSupportReStart": true,
                "IsSupportServiceUpdate": false,
                "IsSupportSubmitConf": true,
                "IsSupportUninstall": false,
                "PathsInfo": "/usr/local/service/zookeeper",
                "ServiceConfStatusNumStatistic": {
                    "ExpiredConfNum": 0,
                    "FailedConfNum": 0
                },
                "ServiceDetectStatus": 1,
                "ServiceNodeList": [
                    {
                        "CoreDeploy": 1,
                        "CoreNecessary": 0,
                        "NodeName": "Zookeeper",
                        "NodeType": 0,
                        "RestartPolicies": [
                            {
                                "BatchSizeRange": [
                                    1,
                                    1
                                ],
                                "Describe": "默认重启模式",
                                "DisplayName": "默认重启模式",
                                "IsDefault": "true",
                                "Name": "default"
                            }
                        ],
                        "TaskDeploy": 0,
                        "TaskNecessary": 0
                    }
                ],
                "ServiceType": 0,
                "SoftName": "ZOOKEEPER",
                "SoftVersion": "3.6.3",
                "Status": 0,
                "UserGroup": "root",
                "UserName": "root",
                "VAddress": "",
                "WebUiDetectStatus": 0,
                "WebUiUrl": "--"
            },
            {
                "AccessInfo": "Filebeat IPC:172.27.16.21:1378;172.27.16.9:1378;172.27.16.112:1378\n",
                "AddTime": "2024-01-30 13:05:59",
                "ClusterId": 52446,
                "CmdServiceOpsInfo": null,
                "ExitInvalidParam": false,
                "IsExternal": false,
                "IsSupportDataMove": false,
                "IsSupportFederation": false,
                "IsSupportMonitor": false,
                "IsSupportReStart": true,
                "IsSupportServiceUpdate": false,
                "IsSupportSubmitConf": true,
                "IsSupportUninstall": false,
                "PathsInfo": "/usr/local/service/filebeat",
                "ServiceConfStatusNumStatistic": {
                    "ExpiredConfNum": 0,
                    "FailedConfNum": 0
                },
                "ServiceDetectStatus": 1,
                "ServiceNodeList": [
                    {
                        "CoreDeploy": 3,
                        "CoreNecessary": 0,
                        "NodeName": "Filebeat",
                        "NodeType": 53,
                        "RestartPolicies": [
                            {
                                "BatchSizeRange": [
                                    1,
                                    99999
                                ],
                                "Describe": "默认重启模式",
                                "DisplayName": "默认重启模式",
                                "IsDefault": "true",
                                "Name": "default"
                            }
                        ],
                        "TaskDeploy": 0,
                        "TaskNecessary": 0
                    }
                ],
                "ServiceType": 25,
                "SoftName": "FILEBEAT",
                "SoftVersion": "7.2.0",
                "Status": 0,
                "UserGroup": "root",
                "UserName": "root",
                "VAddress": "",
                "WebUiDetectStatus": 0,
                "WebUiUrl": "--"
            },
            {
                "AccessInfo": "NameNode IPC:172.27.16.21:4007\nRouter IPC:\nzkfc IPC:\nJournalNode IPC:\nDataNode IPC:172.27.16.9:4001;172.27.16.112:4001\n",
                "AddTime": "2024-01-30 13:05:59",
                "ClusterId": 52446,
                "CmdServiceOpsInfo": null,
                "ExitInvalidParam": false,
                "IsExternal": false,
                "IsSupportDataMove": false,
                "IsSupportFederation": false,
                "IsSupportMonitor": true,
                "IsSupportReStart": true,
                "IsSupportServiceUpdate": false,
                "IsSupportSubmitConf": true,
                "IsSupportUninstall": false,
                "PathsInfo": "/usr/local/service/hadoop",
                "ServiceConfStatusNumStatistic": {
                    "ExpiredConfNum": 0,
                    "FailedConfNum": 0
                },
                "ServiceDetectStatus": 1,
                "ServiceNodeList": [
                    {
                        "CoreDeploy": 1,
                        "CoreNecessary": 0,
                        "NodeName": "NameNode",
                        "NodeType": 1,
                        "RestartPolicies": [
                            {
                                "BatchSizeRange": [
                                    1,
                                    1
                                ],
                                "Describe": "快速重启模式，NameNode通过先stop再start的方式直接重启。",
                                "DisplayName": "快速重启模式",
                                "IsDefault": "true",
                                "Name": "fast"
                            },
                            {
                                "BatchSizeRange": [
                                    1,
                                    1
                                ],
                                "Describe": "安全重启模式，在HA集群中，NameNode先通过standby执行saveNameSpace后，再执行stop,start指令，非HA集群下与快速重启模式无区别",
                                "DisplayName": "安全重启模式",
                                "IsDefault": "false",
                                "Name": "safe"
                            }
                        ],
                        "TaskDeploy": 0,
                        "TaskNecessary": 0
                    },
                    {
                        "CoreDeploy": 2,
                        "CoreNecessary": 0,
                        "NodeName": "DataNode",
                        "NodeType": 2,
                        "RestartPolicies": [
                            {
                                "BatchSizeRange": [
                                    1,
                                    9999
                                ],
                                "Describe": "默认重启模式",
                                "DisplayName": "默认重启模式",
                                "IsDefault": "true",
                                "Name": "default"
                            }
                        ],
                        "TaskDeploy": 0,
                        "TaskNecessary": 0
                    }
                ],
                "ServiceType": 1,
                "SoftName": "HDFS",
                "SoftVersion": "3.2.2",
                "Status": 0,
                "UserGroup": "hadoop",
                "UserName": "hadoop",
                "VAddress": "",
                "WebUiDetectStatus": 1,
                "WebUiUrl": "https://162.14.109.216:30002/gateway/emr/hdfs"
            },
            {
                "AccessInfo": "ResourceManager IPC:172.27.16.21:5004\nNodeManager IPC:172.27.16.9:5006;172.27.16.112:5006\nJobHistoryServer IPC:172.27.16.21:5022\nTimeLineServer IPC:172.27.16.21:8188\n",
                "AddTime": "2024-01-30 13:05:59",
                "ClusterId": 52446,
                "CmdServiceOpsInfo": [
                    {
                        "ActionName": "yarn-refresh-queues",
                        "InterfaceName": "DescribeServiceOps",
                        "OpsName": "刷新队列"
                    }
                ],
                "ExitInvalidParam": false,
                "IsExternal": false,
                "IsSupportDataMove": false,
                "IsSupportFederation": false,
                "IsSupportMonitor": true,
                "IsSupportReStart": true,
                "IsSupportServiceUpdate": false,
                "IsSupportSubmitConf": true,
                "IsSupportUninstall": false,
                "PathsInfo": "/usr/local/service/hadoop",
                "ServiceConfStatusNumStatistic": {
                    "ExpiredConfNum": 0,
                    "FailedConfNum": 0
                },
                "ServiceDetectStatus": 1,
                "ServiceNodeList": [
                    {
                        "CoreDeploy": 1,
                        "CoreNecessary": 0,
                        "NodeName": "ResourceManager",
                        "NodeType": 6,
                        "RestartPolicies": [
                            {
                                "BatchSizeRange": [
                                    1,
                                    1
                                ],
                                "Describe": "默认重启模式",
                                "DisplayName": "默认重启模式",
                                "IsDefault": "true",
                                "Name": "default"
                            }
                        ],
                        "TaskDeploy": 0,
                        "TaskNecessary": 0
                    },
                    {
                        "CoreDeploy": 2,
                        "CoreNecessary": 0,
                        "NodeName": "NodeManager",
                        "NodeType": 7,
                        "RestartPolicies": [
                            {
                                "BatchSizeRange": [
                                    1,
                                    99999
                                ],
                                "Describe": "默认重启模式",
                                "DisplayName": "默认重启模式",
                                "IsDefault": "true",
                                "Name": "default"
                            }
                        ],
                        "TaskDeploy": 0,
                        "TaskNecessary": 0
                    },
                    {
                        "CoreDeploy": 1,
                        "CoreNecessary": 0,
                        "NodeName": "JobHistoryServer",
                        "NodeType": 14,
                        "RestartPolicies": [
                            {
                                "BatchSizeRange": [
                                    1,
                                    99999
                                ],
                                "Describe": "默认重启模式",
                                "DisplayName": "默认重启模式",
                                "IsDefault": "true",
                                "Name": "default"
                            }
                        ],
                        "TaskDeploy": 0,
                        "TaskNecessary": 0
                    },
                    {
                        "CoreDeploy": 1,
                        "CoreNecessary": 0,
                        "NodeName": "TimeLineServer",
                        "NodeType": 102,
                        "RestartPolicies": [
                            {
                                "BatchSizeRange": [
                                    1,
                                    99999
                                ],
                                "Describe": "默认重启模式",
                                "DisplayName": "默认重启模式",
                                "IsDefault": "true",
                                "Name": "default"
                            }
                        ],
                        "TaskDeploy": 0,
                        "TaskNecessary": 0
                    }
                ],
                "ServiceType": 2,
                "SoftName": "YARN",
                "SoftVersion": "3.2.2",
                "Status": 0,
                "UserGroup": "hadoop",
                "UserName": "hadoop",
                "VAddress": "",
                "WebUiDetectStatus": 1,
                "WebUiUrl": "https://162.14.109.216:30002/gateway/emr/yarn"
            },
            {
                "AccessInfo": "HiveMetaStore IPC:172.27.16.21:7004\nHiveServer2 IPC:172.27.16.21:7001\nHiveWebHcat IPC:172.27.16.21:7010\n",
                "AddTime": "2024-01-30 13:05:59",
                "ClusterId": 52446,
                "CmdServiceOpsInfo": null,
                "ExitInvalidParam": false,
                "IsExternal": false,
                "IsSupportDataMove": false,
                "IsSupportFederation": false,
                "IsSupportMonitor": true,
                "IsSupportReStart": true,
                "IsSupportServiceUpdate": false,
                "IsSupportSubmitConf": true,
                "IsSupportUninstall": false,
                "PathsInfo": "/usr/local/service/hive",
                "ServiceConfStatusNumStatistic": {
                    "ExpiredConfNum": 0,
                    "FailedConfNum": 0
                },
                "ServiceDetectStatus": 1,
                "ServiceNodeList": [
                    {
                        "CoreDeploy": 1,
                        "CoreNecessary": 0,
                        "NodeName": "HiveServer2",
                        "NodeType": 31,
                        "RestartPolicies": [
                            {
                                "BatchSizeRange": [
                                    1,
                                    99999
                                ],
                                "Describe": "默认重启模式",
                                "DisplayName": "默认重启模式",
                                "IsDefault": "true",
                                "Name": "default"
                            }
                        ],
                        "TaskDeploy": 0,
                        "TaskNecessary": 0
                    },
                    {
                        "CoreDeploy": 1,
                        "CoreNecessary": 0,
                        "NodeName": "HiveMetaStore",
                        "NodeType": 30,
                        "RestartPolicies": [
                            {
                                "BatchSizeRange": [
                                    1,
                                    99999
                                ],
                                "Describe": "默认重启模式",
                                "DisplayName": "默认重启模式",
                                "IsDefault": "true",
                                "Name": "default"
                            }
                        ],
                        "TaskDeploy": 0,
                        "TaskNecessary": 0
                    },
                    {
                        "CoreDeploy": 1,
                        "CoreNecessary": 0,
                        "NodeName": "HiveWebHcat",
                        "NodeType": 32,
                        "RestartPolicies": [
                            {
                                "BatchSizeRange": [
                                    1,
                                    99999
                                ],
                                "Describe": "默认重启模式",
                                "DisplayName": "默认重启模式",
                                "IsDefault": "true",
                                "Name": "default"
                            }
                        ],
                        "TaskDeploy": 0,
                        "TaskNecessary": 0
                    }
                ],
                "ServiceType": 4,
                "SoftName": "HIVE",
                "SoftVersion": "3.1.3",
                "Status": 0,
                "UserGroup": "hadoop",
                "UserName": "hadoop",
                "VAddress": "",
                "WebUiDetectStatus": 1,
                "WebUiUrl": "https://162.14.109.216:30002/gateway/emr/hive"
            },
            {
                "AccessInfo": "SparkJobHistoryServer IPC:172.27.16.21:10000\n",
                "AddTime": "2024-01-30 13:05:59",
                "ClusterId": 52446,
                "CmdServiceOpsInfo": null,
                "ExitInvalidParam": false,
                "IsExternal": false,
                "IsSupportDataMove": false,
                "IsSupportFederation": false,
                "IsSupportMonitor": true,
                "IsSupportReStart": true,
                "IsSupportServiceUpdate": false,
                "IsSupportSubmitConf": true,
                "IsSupportUninstall": false,
                "PathsInfo": "/usr/local/service/spark",
                "ServiceConfStatusNumStatistic": {
                    "ExpiredConfNum": 0,
                    "FailedConfNum": 0
                },
                "ServiceDetectStatus": 1,
                "ServiceNodeList": [
                    {
                        "CoreDeploy": 1,
                        "CoreNecessary": 0,
                        "NodeName": "SparkJobHistoryServer",
                        "NodeType": 17,
                        "RestartPolicies": [
                            {
                                "BatchSizeRange": [
                                    1,
                                    99999
                                ],
                                "Describe": "默认重启模式",
                                "DisplayName": "默认重启模式",
                                "IsDefault": "true",
                                "Name": "default"
                            }
                        ],
                        "TaskDeploy": 0,
                        "TaskNecessary": 0
                    }
                ],
                "ServiceType": 6,
                "SoftName": "SPARK",
                "SoftVersion": "3.2.2",
                "Status": 0,
                "UserGroup": "hadoop",
                "UserName": "hadoop",
                "VAddress": "",
                "WebUiDetectStatus": 1,
                "WebUiUrl": "https://162.14.109.216:30002/gateway/emr/sparkhistory/"
            },
            {
                "AccessInfo": "Gateway IPC:172.27.16.21:30002\nLdap IPC:172.27.16.21:33389\n",
                "AddTime": "2024-01-30 13:05:59",
                "ClusterId": 52446,
                "CmdServiceOpsInfo": null,
                "ExitInvalidParam": false,
                "IsExternal": false,
                "IsSupportDataMove": false,
                "IsSupportFederation": false,
                "IsSupportMonitor": false,
                "IsSupportReStart": false,
                "IsSupportServiceUpdate": false,
                "IsSupportSubmitConf": false,
                "IsSupportUninstall": false,
                "PathsInfo": "/usr/local/service/knox",
                "ServiceConfStatusNumStatistic": {
                    "ExpiredConfNum": 0,
                    "FailedConfNum": 0
                },
                "ServiceDetectStatus": 1,
                "ServiceNodeList": [
                    {
                        "CoreDeploy": 1,
                        "CoreNecessary": 0,
                        "NodeName": "knox",
                        "NodeType": 50,
                        "RestartPolicies": [
                            {
                                "BatchSizeRange": [
                                    1,
                                    99999
                                ],
                                "Describe": "默认重启模式",
                                "DisplayName": "默认重启模式",
                                "IsDefault": "true",
                                "Name": "default"
                            }
                        ],
                        "TaskDeploy": 0,
                        "TaskNecessary": 0
                    }
                ],
                "ServiceType": 24,
                "SoftName": "KNOX",
                "SoftVersion": "1.6.1",
                "Status": 0,
                "UserGroup": "hadoop",
                "UserName": "hadoop",
                "VAddress": "",
                "WebUiDetectStatus": 0,
                "WebUiUrl": "--"
            },
            {
                "AccessInfo": "KyuubiServer IPC:172.27.16.21:10009\n",
                "AddTime": "2024-01-30 13:05:59",
                "ClusterId": 52446,
                "CmdServiceOpsInfo": null,
                "ExitInvalidParam": false,
                "IsExternal": false,
                "IsSupportDataMove": false,
                "IsSupportFederation": false,
                "IsSupportMonitor": true,
                "IsSupportReStart": true,
                "IsSupportServiceUpdate": false,
                "IsSupportSubmitConf": true,
                "IsSupportUninstall": true,
                "PathsInfo": "/usr/local/service/kyuubi",
                "ServiceConfStatusNumStatistic": {
                    "ExpiredConfNum": 0,
                    "FailedConfNum": 0
                },
                "ServiceDetectStatus": 1,
                "ServiceNodeList": [
                    {
                        "CoreDeploy": 1,
                        "CoreNecessary": 0,
                        "NodeName": "KyuubiServer",
                        "NodeType": 87,
                        "RestartPolicies": [
                            {
                                "BatchSizeRange": [
                                    1,
                                    99999
                                ],
                                "Describe": "默认重启模式",
                                "DisplayName": "默认重启模式",
                                "IsDefault": "true",
                                "Name": "default"
                            }
                        ],
                        "TaskDeploy": 0,
                        "TaskNecessary": 0
                    }
                ],
                "ServiceType": 22,
                "SoftName": "KYUUBI",
                "SoftVersion": "1.6.0",
                "Status": 0,
                "UserGroup": "hadoop",
                "UserName": "hadoop",
                "VAddress": "",
                "WebUiDetectStatus": 0,
                "WebUiUrl": "--"
            },
            {
                "AccessInfo": "Ranger IPC:172.27.16.21:6080\nRangerUsersync IPC:172.27.16.21:5151\nSolr IPC:172.27.16.21:6083\n",
                "AddTime": "2024-01-30 13:05:59",
                "ClusterId": 52446,
                "CmdServiceOpsInfo": null,
                "ExitInvalidParam": false,
                "IsExternal": false,
                "IsSupportDataMove": false,
                "IsSupportFederation": false,
                "IsSupportMonitor": true,
                "IsSupportReStart": true,
                "IsSupportServiceUpdate": false,
                "IsSupportSubmitConf": true,
                "IsSupportUninstall": false,
                "PathsInfo": "/usr/local/service/ranger",
                "ServiceConfStatusNumStatistic": {
                    "ExpiredConfNum": 0,
                    "FailedConfNum": 0
                },
                "ServiceDetectStatus": 1,
                "ServiceNodeList": [
                    {
                        "CoreDeploy": 1,
                        "CoreNecessary": 0,
                        "NodeName": "EmbeddedServer",
                        "NodeType": 28,
                        "RestartPolicies": [
                            {
                                "BatchSizeRange": [
                                    1,
                                    99999
                                ],
                                "Describe": "默认重启模式",
                                "DisplayName": "默认重启模式",
                                "IsDefault": "true",
                                "Name": "default"
                            }
                        ],
                        "TaskDeploy": 0,
                        "TaskNecessary": 0
                    },
                    {
                        "CoreDeploy": 1,
                        "CoreNecessary": 0,
                        "NodeName": "EnableUnixAuth",
                        "NodeType": 68,
                        "RestartPolicies": [
                            {
                                "BatchSizeRange": [
                                    1,
                                    99999
                                ],
                                "Describe": "默认重启模式",
                                "DisplayName": "默认重启模式",
                                "IsDefault": "true",
                                "Name": "default"
                            }
                        ],
                        "TaskDeploy": 0,
                        "TaskNecessary": 0
                    },
                    {
                        "CoreDeploy": 1,
                        "CoreNecessary": 0,
                        "NodeName": "Solr",
                        "NodeType": 95,
                        "RestartPolicies": [
                            {
                                "BatchSizeRange": [
                                    1,
                                    99999
                                ],
                                "Describe": "默认重启模式",
                                "DisplayName": "默认重启模式",
                                "IsDefault": "true",
                                "Name": "default"
                            }
                        ],
                        "TaskDeploy": 0,
                        "TaskNecessary": 0
                    }
                ],
                "ServiceType": 16,
                "SoftName": "RANGER",
                "SoftVersion": "2.3.0",
                "Status": 0,
                "UserGroup": "root",
                "UserName": "root",
                "VAddress": "",
                "WebUiDetectStatus": 1,
                "WebUiUrl": "https://162.14.109.216:30002/gateway/emr/ranger/"
            }
        ],
        "TotalCnt": 11
    }
}
```

