**Example 1: 查询**



Input: 

```
tccli bi DescribeResourceUserGroupPageList --cli-unfold-argument  \
    --ProjectId 674 \
    --PageId 2840 \
    --PageSize 10 \
    --PageNo 0 \
    --AllPage 1 \
    --Keyword  \
    --ResourceType page \
    --EntityId 2840 \
    --ParentId -1 \
    --ResourceName  \
    --ModuleCollection  \
    --ResourceValue 
```

Output: 
```
{
    "Response": {
        "Msg": "默认业务成功",
        "RequestId": "HFR6l3QX-WnwI-4_Tk-8JCL-k-l6tQDNUSe9GX4-",
        "Extra": "",
        "Data": {
            "List": [
                {
                    "Id": 8,
                    "GroupName": "CSIG云与智慧产业事业群",
                    "ParentId": -1,
                    "ParentName": null,
                    "IsDefault": 0,
                    "AdminUserId": "hookeye",
                    "UserList": null,
                    "Description": "",
                    "Location": 6,
                    "Children": [
                        {
                            "Id": 11,
                            "GroupName": "云产品一部",
                            "ParentId": 8,
                            "ParentName": null,
                            "IsDefault": 0,
                            "AdminUserId": "hookeye",
                            "UserList": null,
                            "Description": null,
                            "Location": 0,
                            "Children": [
                                {
                                    "Id": 108,
                                    "GroupName": "ssss",
                                    "ParentId": 11,
                                    "ParentName": null,
                                    "IsDefault": 0,
                                    "AdminUserId": "sunnyyyli",
                                    "UserList": null,
                                    "Description": null,
                                    "Location": 1,
                                    "Children": [
                                        {
                                            "Id": 97,
                                            "GroupName": "g1",
                                            "ParentId": 108,
                                            "ParentName": null,
                                            "IsDefault": 0,
                                            "AdminUserId": "samjzhang",
                                            "UserList": null,
                                            "Description": "",
                                            "Location": 0,
                                            "Children": [
                                                {
                                                    "Id": 21,
                                                    "GroupName": "dsafdsa ",
                                                    "ParentId": 97,
                                                    "ParentName": null,
                                                    "IsDefault": 0,
                                                    "AdminUserId": "hookeye",
                                                    "UserList": null,
                                                    "Description": null,
                                                    "Location": 0,
                                                    "Children": null,
                                                    "HasChildren": false,
                                                    "ResourceList": [
                                                        {
                                                            "ResourceName": "PageEdit",
                                                            "ResourceValue": false,
                                                            "CanChange": true,
                                                            "Tips": ""
                                                        },
                                                        {
                                                            "ResourceName": "PageRetrieval",
                                                            "ResourceValue": false,
                                                            "CanChange": true,
                                                            "Tips": ""
                                                        },
                                                        {
                                                            "ResourceName": "PageExport",
                                                            "ResourceValue": false,
                                                            "CanChange": true,
                                                            "Tips": ""
                                                        },
                                                        {
                                                            "ResourceName": "PageShareAndIframe",
                                                            "ResourceValue": false,
                                                            "CanChange": true,
                                                            "Tips": ""
                                                        },
                                                        {
                                                            "ResourceName": "PageView",
                                                            "ResourceValue": false,
                                                            "CanChange": true,
                                                            "Tips": ""
                                                        }
                                                    ]
                                                }
                                            ],
                                            "HasChildren": true,
                                            "ResourceList": [
                                                {
                                                    "ResourceName": "PageEdit",
                                                    "ResourceValue": false,
                                                    "CanChange": true,
                                                    "Tips": ""
                                                },
                                                {
                                                    "ResourceName": "PageRetrieval",
                                                    "ResourceValue": false,
                                                    "CanChange": true,
                                                    "Tips": ""
                                                },
                                                {
                                                    "ResourceName": "PageExport",
                                                    "ResourceValue": false,
                                                    "CanChange": true,
                                                    "Tips": ""
                                                },
                                                {
                                                    "ResourceName": "PageShareAndIframe",
                                                    "ResourceValue": false,
                                                    "CanChange": true,
                                                    "Tips": ""
                                                },
                                                {
                                                    "ResourceName": "PageView",
                                                    "ResourceValue": false,
                                                    "CanChange": true,
                                                    "Tips": ""
                                                }
                                            ]
                                        }
                                    ],
                                    "HasChildren": true,
                                    "ResourceList": [
                                        {
                                            "ResourceName": "PageEdit",
                                            "ResourceValue": false,
                                            "CanChange": true,
                                            "Tips": ""
                                        },
                                        {
                                            "ResourceName": "PageRetrieval",
                                            "ResourceValue": false,
                                            "CanChange": true,
                                            "Tips": ""
                                        },
                                        {
                                            "ResourceName": "PageExport",
                                            "ResourceValue": false,
                                            "CanChange": true,
                                            "Tips": ""
                                        },
                                        {
                                            "ResourceName": "PageShareAndIframe",
                                            "ResourceValue": false,
                                            "CanChange": true,
                                            "Tips": ""
                                        },
                                        {
                                            "ResourceName": "PageView",
                                            "ResourceValue": false,
                                            "CanChange": true,
                                            "Tips": ""
                                        }
                                    ]
                                }
                            ],
                            "HasChildren": true,
                            "ResourceList": [
                                {
                                    "ResourceName": "PageEdit",
                                    "ResourceValue": false,
                                    "CanChange": true,
                                    "Tips": ""
                                },
                                {
                                    "ResourceName": "PageRetrieval",
                                    "ResourceValue": false,
                                    "CanChange": true,
                                    "Tips": ""
                                },
                                {
                                    "ResourceName": "PageExport",
                                    "ResourceValue": false,
                                    "CanChange": true,
                                    "Tips": ""
                                },
                                {
                                    "ResourceName": "PageShareAndIframe",
                                    "ResourceValue": false,
                                    "CanChange": true,
                                    "Tips": ""
                                },
                                {
                                    "ResourceName": "PageView",
                                    "ResourceValue": false,
                                    "CanChange": true,
                                    "Tips": ""
                                }
                            ]
                        }
                    ],
                    "HasChildren": true,
                    "ResourceList": [
                        {
                            "ResourceName": "PageEdit",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageRetrieval",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageExport",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageShareAndIframe",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageView",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        }
                    ]
                },
                {
                    "Id": 12,
                    "GroupName": "总办",
                    "ParentId": -1,
                    "ParentName": null,
                    "IsDefault": 0,
                    "AdminUserId": "hookeye",
                    "UserList": null,
                    "Description": null,
                    "Location": 1,
                    "Children": null,
                    "HasChildren": false,
                    "ResourceList": [
                        {
                            "ResourceName": "PageEdit",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageRetrieval",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageExport",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageShareAndIframe",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageView",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        }
                    ]
                },
                {
                    "Id": 15,
                    "GroupName": "IEG互动娱乐事业群",
                    "ParentId": -1,
                    "ParentName": null,
                    "IsDefault": 0,
                    "AdminUserId": "hookeye",
                    "UserList": null,
                    "Description": null,
                    "Location": 3,
                    "Children": null,
                    "HasChildren": false,
                    "ResourceList": [
                        {
                            "ResourceName": "PageEdit",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageRetrieval",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageExport",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageShareAndIframe",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageView",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        }
                    ]
                },
                {
                    "Id": 18,
                    "GroupName": "TEG技术工程事业群",
                    "ParentId": -1,
                    "ParentName": null,
                    "IsDefault": 0,
                    "AdminUserId": "hookeye",
                    "UserList": null,
                    "Description": null,
                    "Location": 5,
                    "Children": null,
                    "HasChildren": false,
                    "ResourceList": [
                        {
                            "ResourceName": "PageEdit",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageRetrieval",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageExport",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageShareAndIframe",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageView",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        }
                    ]
                },
                {
                    "Id": 20,
                    "GroupName": "PCG平台与内容事业群",
                    "ParentId": -1,
                    "ParentName": null,
                    "IsDefault": 0,
                    "AdminUserId": "hookeye",
                    "UserList": null,
                    "Description": null,
                    "Location": 4,
                    "Children": null,
                    "HasChildren": false,
                    "ResourceList": [
                        {
                            "ResourceName": "PageEdit",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageRetrieval",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageExport",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageShareAndIframe",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageView",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        }
                    ]
                },
                {
                    "Id": 23,
                    "GroupName": "这个是测试的一级用户组这个是测试的一级用户组这个是测试的一级用户组这个是测试的一级用户组这个是测试的",
                    "ParentId": -1,
                    "ParentName": null,
                    "IsDefault": 0,
                    "AdminUserId": "samjzhang",
                    "UserList": null,
                    "Description": "这个是测试的一级用户组",
                    "Location": 12,
                    "Children": null,
                    "HasChildren": false,
                    "ResourceList": [
                        {
                            "ResourceName": "PageEdit",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageRetrieval",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageExport",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageShareAndIframe",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageView",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        }
                    ]
                },
                {
                    "Id": 38,
                    "GroupName": "云产品一部",
                    "ParentId": -1,
                    "ParentName": null,
                    "IsDefault": 0,
                    "AdminUserId": "samjzhang",
                    "UserList": null,
                    "Description": null,
                    "Location": 14,
                    "Children": [
                        {
                            "Id": 45,
                            "GroupName": "S线",
                            "ParentId": 38,
                            "ParentName": null,
                            "IsDefault": 0,
                            "AdminUserId": "samjzhang",
                            "UserList": null,
                            "Description": "",
                            "Location": 0,
                            "Children": [
                                {
                                    "Id": 54,
                                    "GroupName": "测试二级用户组3",
                                    "ParentId": 45,
                                    "ParentName": null,
                                    "IsDefault": 0,
                                    "AdminUserId": "samjzhang",
                                    "UserList": null,
                                    "Description": null,
                                    "Location": 0,
                                    "Children": [
                                        {
                                            "Id": 28,
                                            "GroupName": "一级部门用户组1",
                                            "ParentId": 54,
                                            "ParentName": null,
                                            "IsDefault": 0,
                                            "AdminUserId": "samjzhang,909619400",
                                            "UserList": null,
                                            "Description": "",
                                            "Location": 0,
                                            "Children": [
                                                {
                                                    "Id": 58,
                                                    "GroupName": "五级用户组",
                                                    "ParentId": 28,
                                                    "ParentName": null,
                                                    "IsDefault": 0,
                                                    "AdminUserId": "samjzhang,huangshaowu",
                                                    "UserList": null,
                                                    "Description": null,
                                                    "Location": 0,
                                                    "Children": null,
                                                    "HasChildren": false,
                                                    "ResourceList": [
                                                        {
                                                            "ResourceName": "PageEdit",
                                                            "ResourceValue": false,
                                                            "CanChange": true,
                                                            "Tips": ""
                                                        },
                                                        {
                                                            "ResourceName": "PageRetrieval",
                                                            "ResourceValue": false,
                                                            "CanChange": true,
                                                            "Tips": ""
                                                        },
                                                        {
                                                            "ResourceName": "PageExport",
                                                            "ResourceValue": false,
                                                            "CanChange": true,
                                                            "Tips": ""
                                                        },
                                                        {
                                                            "ResourceName": "PageShareAndIframe",
                                                            "ResourceValue": false,
                                                            "CanChange": true,
                                                            "Tips": ""
                                                        },
                                                        {
                                                            "ResourceName": "PageView",
                                                            "ResourceValue": false,
                                                            "CanChange": true,
                                                            "Tips": ""
                                                        }
                                                    ]
                                                }
                                            ],
                                            "HasChildren": true,
                                            "ResourceList": [
                                                {
                                                    "ResourceName": "PageEdit",
                                                    "ResourceValue": false,
                                                    "CanChange": true,
                                                    "Tips": ""
                                                },
                                                {
                                                    "ResourceName": "PageRetrieval",
                                                    "ResourceValue": false,
                                                    "CanChange": true,
                                                    "Tips": ""
                                                },
                                                {
                                                    "ResourceName": "PageExport",
                                                    "ResourceValue": false,
                                                    "CanChange": true,
                                                    "Tips": ""
                                                },
                                                {
                                                    "ResourceName": "PageShareAndIframe",
                                                    "ResourceValue": false,
                                                    "CanChange": true,
                                                    "Tips": ""
                                                },
                                                {
                                                    "ResourceName": "PageView",
                                                    "ResourceValue": false,
                                                    "CanChange": true,
                                                    "Tips": ""
                                                }
                                            ]
                                        }
                                    ],
                                    "HasChildren": true,
                                    "ResourceList": [
                                        {
                                            "ResourceName": "PageEdit",
                                            "ResourceValue": false,
                                            "CanChange": true,
                                            "Tips": ""
                                        },
                                        {
                                            "ResourceName": "PageRetrieval",
                                            "ResourceValue": false,
                                            "CanChange": true,
                                            "Tips": ""
                                        },
                                        {
                                            "ResourceName": "PageExport",
                                            "ResourceValue": false,
                                            "CanChange": true,
                                            "Tips": ""
                                        },
                                        {
                                            "ResourceName": "PageShareAndIframe",
                                            "ResourceValue": false,
                                            "CanChange": true,
                                            "Tips": ""
                                        },
                                        {
                                            "ResourceName": "PageView",
                                            "ResourceValue": false,
                                            "CanChange": true,
                                            "Tips": ""
                                        }
                                    ]
                                },
                                {
                                    "Id": 111,
                                    "GroupName": "11",
                                    "ParentId": 45,
                                    "ParentName": null,
                                    "IsDefault": 0,
                                    "AdminUserId": "sunnyyyli",
                                    "UserList": null,
                                    "Description": "",
                                    "Location": 1,
                                    "Children": null,
                                    "HasChildren": false,
                                    "ResourceList": [
                                        {
                                            "ResourceName": "PageEdit",
                                            "ResourceValue": false,
                                            "CanChange": true,
                                            "Tips": ""
                                        },
                                        {
                                            "ResourceName": "PageRetrieval",
                                            "ResourceValue": false,
                                            "CanChange": true,
                                            "Tips": ""
                                        },
                                        {
                                            "ResourceName": "PageExport",
                                            "ResourceValue": false,
                                            "CanChange": true,
                                            "Tips": ""
                                        },
                                        {
                                            "ResourceName": "PageShareAndIframe",
                                            "ResourceValue": false,
                                            "CanChange": true,
                                            "Tips": ""
                                        },
                                        {
                                            "ResourceName": "PageView",
                                            "ResourceValue": false,
                                            "CanChange": true,
                                            "Tips": ""
                                        }
                                    ]
                                }
                            ],
                            "HasChildren": true,
                            "ResourceList": [
                                {
                                    "ResourceName": "PageEdit",
                                    "ResourceValue": false,
                                    "CanChange": true,
                                    "Tips": ""
                                },
                                {
                                    "ResourceName": "PageRetrieval",
                                    "ResourceValue": false,
                                    "CanChange": true,
                                    "Tips": ""
                                },
                                {
                                    "ResourceName": "PageExport",
                                    "ResourceValue": false,
                                    "CanChange": true,
                                    "Tips": ""
                                },
                                {
                                    "ResourceName": "PageShareAndIframe",
                                    "ResourceValue": false,
                                    "CanChange": true,
                                    "Tips": ""
                                },
                                {
                                    "ResourceName": "PageView",
                                    "ResourceValue": false,
                                    "CanChange": true,
                                    "Tips": ""
                                }
                            ]
                        },
                        {
                            "Id": 46,
                            "GroupName": "测试一级用户组",
                            "ParentId": 38,
                            "ParentName": null,
                            "IsDefault": 0,
                            "AdminUserId": "samjzhang",
                            "UserList": null,
                            "Description": null,
                            "Location": 1,
                            "Children": [
                                {
                                    "Id": 114,
                                    "GroupName": "ssss",
                                    "ParentId": 46,
                                    "ParentName": null,
                                    "IsDefault": 0,
                                    "AdminUserId": "sunnyyyli",
                                    "UserList": null,
                                    "Description": null,
                                    "Location": 0,
                                    "Children": [
                                        {
                                            "Id": 117,
                                            "GroupName": "22",
                                            "ParentId": 114,
                                            "ParentName": null,
                                            "IsDefault": 0,
                                            "AdminUserId": "sunnyyyli",
                                            "UserList": null,
                                            "Description": null,
                                            "Location": 0,
                                            "Children": [
                                                {
                                                    "Id": 125,
                                                    "GroupName": "1222",
                                                    "ParentId": 117,
                                                    "ParentName": null,
                                                    "IsDefault": 0,
                                                    "AdminUserId": "samjzhang",
                                                    "UserList": null,
                                                    "Description": "",
                                                    "Location": 0,
                                                    "Children": null,
                                                    "HasChildren": false,
                                                    "ResourceList": [
                                                        {
                                                            "ResourceName": "PageEdit",
                                                            "ResourceValue": false,
                                                            "CanChange": true,
                                                            "Tips": ""
                                                        },
                                                        {
                                                            "ResourceName": "PageRetrieval",
                                                            "ResourceValue": false,
                                                            "CanChange": true,
                                                            "Tips": ""
                                                        },
                                                        {
                                                            "ResourceName": "PageExport",
                                                            "ResourceValue": false,
                                                            "CanChange": true,
                                                            "Tips": ""
                                                        },
                                                        {
                                                            "ResourceName": "PageShareAndIframe",
                                                            "ResourceValue": false,
                                                            "CanChange": true,
                                                            "Tips": ""
                                                        },
                                                        {
                                                            "ResourceName": "PageView",
                                                            "ResourceValue": false,
                                                            "CanChange": true,
                                                            "Tips": ""
                                                        }
                                                    ]
                                                }
                                            ],
                                            "HasChildren": true,
                                            "ResourceList": [
                                                {
                                                    "ResourceName": "PageEdit",
                                                    "ResourceValue": false,
                                                    "CanChange": true,
                                                    "Tips": ""
                                                },
                                                {
                                                    "ResourceName": "PageRetrieval",
                                                    "ResourceValue": false,
                                                    "CanChange": true,
                                                    "Tips": ""
                                                },
                                                {
                                                    "ResourceName": "PageExport",
                                                    "ResourceValue": false,
                                                    "CanChange": true,
                                                    "Tips": ""
                                                },
                                                {
                                                    "ResourceName": "PageShareAndIframe",
                                                    "ResourceValue": false,
                                                    "CanChange": true,
                                                    "Tips": ""
                                                },
                                                {
                                                    "ResourceName": "PageView",
                                                    "ResourceValue": false,
                                                    "CanChange": true,
                                                    "Tips": ""
                                                }
                                            ]
                                        }
                                    ],
                                    "HasChildren": true,
                                    "ResourceList": [
                                        {
                                            "ResourceName": "PageEdit",
                                            "ResourceValue": false,
                                            "CanChange": true,
                                            "Tips": ""
                                        },
                                        {
                                            "ResourceName": "PageRetrieval",
                                            "ResourceValue": false,
                                            "CanChange": true,
                                            "Tips": ""
                                        },
                                        {
                                            "ResourceName": "PageExport",
                                            "ResourceValue": false,
                                            "CanChange": true,
                                            "Tips": ""
                                        },
                                        {
                                            "ResourceName": "PageShareAndIframe",
                                            "ResourceValue": false,
                                            "CanChange": true,
                                            "Tips": ""
                                        },
                                        {
                                            "ResourceName": "PageView",
                                            "ResourceValue": false,
                                            "CanChange": true,
                                            "Tips": ""
                                        }
                                    ]
                                }
                            ],
                            "HasChildren": true,
                            "ResourceList": [
                                {
                                    "ResourceName": "PageEdit",
                                    "ResourceValue": false,
                                    "CanChange": true,
                                    "Tips": ""
                                },
                                {
                                    "ResourceName": "PageRetrieval",
                                    "ResourceValue": false,
                                    "CanChange": true,
                                    "Tips": ""
                                },
                                {
                                    "ResourceName": "PageExport",
                                    "ResourceValue": false,
                                    "CanChange": true,
                                    "Tips": ""
                                },
                                {
                                    "ResourceName": "PageShareAndIframe",
                                    "ResourceValue": false,
                                    "CanChange": true,
                                    "Tips": ""
                                },
                                {
                                    "ResourceName": "PageView",
                                    "ResourceValue": false,
                                    "CanChange": true,
                                    "Tips": ""
                                }
                            ]
                        }
                    ],
                    "HasChildren": true,
                    "ResourceList": [
                        {
                            "ResourceName": "PageEdit",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageRetrieval",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageExport",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageShareAndIframe",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageView",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        }
                    ]
                },
                {
                    "Id": 42,
                    "GroupName": "S线1",
                    "ParentId": -1,
                    "ParentName": null,
                    "IsDefault": 0,
                    "AdminUserId": "samjzhang",
                    "UserList": null,
                    "Description": "",
                    "Location": 13,
                    "Children": null,
                    "HasChildren": false,
                    "ResourceList": [
                        {
                            "ResourceName": "PageEdit",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageRetrieval",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageExport",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageShareAndIframe",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageView",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        }
                    ]
                },
                {
                    "Id": 57,
                    "GroupName": "测试二级用户组",
                    "ParentId": -1,
                    "ParentName": null,
                    "IsDefault": 0,
                    "AdminUserId": "samjzhang,909619400,huangshaowu,hookeye,bi_viewer_user,mayxxiao,damonyyu,samjzhang3",
                    "UserList": null,
                    "Description": "",
                    "Location": 2,
                    "Children": [
                        {
                            "Id": 49,
                            "GroupName": "测试二级用户组1",
                            "ParentId": 57,
                            "ParentName": null,
                            "IsDefault": 0,
                            "AdminUserId": "samjzhang",
                            "UserList": null,
                            "Description": "",
                            "Location": 0,
                            "Children": null,
                            "HasChildren": false,
                            "ResourceList": [
                                {
                                    "ResourceName": "PageEdit",
                                    "ResourceValue": false,
                                    "CanChange": true,
                                    "Tips": ""
                                },
                                {
                                    "ResourceName": "PageRetrieval",
                                    "ResourceValue": false,
                                    "CanChange": true,
                                    "Tips": ""
                                },
                                {
                                    "ResourceName": "PageExport",
                                    "ResourceValue": false,
                                    "CanChange": true,
                                    "Tips": ""
                                },
                                {
                                    "ResourceName": "PageShareAndIframe",
                                    "ResourceValue": false,
                                    "CanChange": true,
                                    "Tips": ""
                                },
                                {
                                    "ResourceName": "PageView",
                                    "ResourceValue": false,
                                    "CanChange": true,
                                    "Tips": ""
                                }
                            ]
                        },
                        {
                            "Id": 59,
                            "GroupName": "测试二级用户组",
                            "ParentId": 57,
                            "ParentName": null,
                            "IsDefault": 0,
                            "AdminUserId": "samjzhang",
                            "UserList": null,
                            "Description": null,
                            "Location": 1,
                            "Children": [
                                {
                                    "Id": 62,
                                    "GroupName": "测试3级用户组",
                                    "ParentId": 59,
                                    "ParentName": null,
                                    "IsDefault": 0,
                                    "AdminUserId": "samjzhang",
                                    "UserList": null,
                                    "Description": null,
                                    "Location": 1,
                                    "Children": [
                                        {
                                            "Id": 66,
                                            "GroupName": "测试4级用户组1",
                                            "ParentId": 62,
                                            "ParentName": null,
                                            "IsDefault": 0,
                                            "AdminUserId": "samjzhang",
                                            "UserList": null,
                                            "Description": null,
                                            "Location": 0,
                                            "Children": [
                                                {
                                                    "Id": 65,
                                                    "GroupName": "测试4级用户组",
                                                    "ParentId": 66,
                                                    "ParentName": null,
                                                    "IsDefault": 0,
                                                    "AdminUserId": "samjzhang",
                                                    "UserList": null,
                                                    "Description": null,
                                                    "Location": 0,
                                                    "Children": null,
                                                    "HasChildren": false,
                                                    "ResourceList": [
                                                        {
                                                            "ResourceName": "PageEdit",
                                                            "ResourceValue": false,
                                                            "CanChange": true,
                                                            "Tips": ""
                                                        },
                                                        {
                                                            "ResourceName": "PageRetrieval",
                                                            "ResourceValue": false,
                                                            "CanChange": true,
                                                            "Tips": ""
                                                        },
                                                        {
                                                            "ResourceName": "PageExport",
                                                            "ResourceValue": false,
                                                            "CanChange": true,
                                                            "Tips": ""
                                                        },
                                                        {
                                                            "ResourceName": "PageShareAndIframe",
                                                            "ResourceValue": false,
                                                            "CanChange": true,
                                                            "Tips": ""
                                                        },
                                                        {
                                                            "ResourceName": "PageView",
                                                            "ResourceValue": false,
                                                            "CanChange": true,
                                                            "Tips": ""
                                                        }
                                                    ]
                                                },
                                                {
                                                    "Id": 69,
                                                    "GroupName": "测试5级用户组",
                                                    "ParentId": 66,
                                                    "ParentName": null,
                                                    "IsDefault": 0,
                                                    "AdminUserId": "samjzhang",
                                                    "UserList": null,
                                                    "Description": "",
                                                    "Location": 1,
                                                    "Children": null,
                                                    "HasChildren": false,
                                                    "ResourceList": [
                                                        {
                                                            "ResourceName": "PageEdit",
                                                            "ResourceValue": false,
                                                            "CanChange": true,
                                                            "Tips": ""
                                                        },
                                                        {
                                                            "ResourceName": "PageRetrieval",
                                                            "ResourceValue": false,
                                                            "CanChange": true,
                                                            "Tips": ""
                                                        },
                                                        {
                                                            "ResourceName": "PageExport",
                                                            "ResourceValue": false,
                                                            "CanChange": true,
                                                            "Tips": ""
                                                        },
                                                        {
                                                            "ResourceName": "PageShareAndIframe",
                                                            "ResourceValue": false,
                                                            "CanChange": true,
                                                            "Tips": ""
                                                        },
                                                        {
                                                            "ResourceName": "PageView",
                                                            "ResourceValue": false,
                                                            "CanChange": true,
                                                            "Tips": ""
                                                        }
                                                    ]
                                                }
                                            ],
                                            "HasChildren": true,
                                            "ResourceList": [
                                                {
                                                    "ResourceName": "PageEdit",
                                                    "ResourceValue": false,
                                                    "CanChange": true,
                                                    "Tips": ""
                                                },
                                                {
                                                    "ResourceName": "PageRetrieval",
                                                    "ResourceValue": false,
                                                    "CanChange": true,
                                                    "Tips": ""
                                                },
                                                {
                                                    "ResourceName": "PageExport",
                                                    "ResourceValue": false,
                                                    "CanChange": true,
                                                    "Tips": ""
                                                },
                                                {
                                                    "ResourceName": "PageShareAndIframe",
                                                    "ResourceValue": false,
                                                    "CanChange": true,
                                                    "Tips": ""
                                                },
                                                {
                                                    "ResourceName": "PageView",
                                                    "ResourceValue": false,
                                                    "CanChange": true,
                                                    "Tips": ""
                                                }
                                            ]
                                        }
                                    ],
                                    "HasChildren": true,
                                    "ResourceList": [
                                        {
                                            "ResourceName": "PageEdit",
                                            "ResourceValue": false,
                                            "CanChange": true,
                                            "Tips": ""
                                        },
                                        {
                                            "ResourceName": "PageRetrieval",
                                            "ResourceValue": false,
                                            "CanChange": true,
                                            "Tips": ""
                                        },
                                        {
                                            "ResourceName": "PageExport",
                                            "ResourceValue": false,
                                            "CanChange": true,
                                            "Tips": ""
                                        },
                                        {
                                            "ResourceName": "PageShareAndIframe",
                                            "ResourceValue": false,
                                            "CanChange": true,
                                            "Tips": ""
                                        },
                                        {
                                            "ResourceName": "PageView",
                                            "ResourceValue": false,
                                            "CanChange": true,
                                            "Tips": ""
                                        }
                                    ]
                                },
                                {
                                    "Id": 63,
                                    "GroupName": "测试3级用户组1",
                                    "ParentId": 59,
                                    "ParentName": null,
                                    "IsDefault": 0,
                                    "AdminUserId": "samjzhang,909619400,damonyyu",
                                    "UserList": null,
                                    "Description": "",
                                    "Location": 2,
                                    "Children": null,
                                    "HasChildren": false,
                                    "ResourceList": [
                                        {
                                            "ResourceName": "PageEdit",
                                            "ResourceValue": false,
                                            "CanChange": true,
                                            "Tips": ""
                                        },
                                        {
                                            "ResourceName": "PageRetrieval",
                                            "ResourceValue": false,
                                            "CanChange": true,
                                            "Tips": ""
                                        },
                                        {
                                            "ResourceName": "PageExport",
                                            "ResourceValue": false,
                                            "CanChange": true,
                                            "Tips": ""
                                        },
                                        {
                                            "ResourceName": "PageShareAndIframe",
                                            "ResourceValue": false,
                                            "CanChange": true,
                                            "Tips": ""
                                        },
                                        {
                                            "ResourceName": "PageView",
                                            "ResourceValue": false,
                                            "CanChange": true,
                                            "Tips": ""
                                        }
                                    ]
                                }
                            ],
                            "HasChildren": true,
                            "ResourceList": [
                                {
                                    "ResourceName": "PageEdit",
                                    "ResourceValue": false,
                                    "CanChange": true,
                                    "Tips": ""
                                },
                                {
                                    "ResourceName": "PageRetrieval",
                                    "ResourceValue": false,
                                    "CanChange": true,
                                    "Tips": ""
                                },
                                {
                                    "ResourceName": "PageExport",
                                    "ResourceValue": false,
                                    "CanChange": true,
                                    "Tips": ""
                                },
                                {
                                    "ResourceName": "PageShareAndIframe",
                                    "ResourceValue": false,
                                    "CanChange": true,
                                    "Tips": ""
                                },
                                {
                                    "ResourceName": "PageView",
                                    "ResourceValue": false,
                                    "CanChange": true,
                                    "Tips": ""
                                }
                            ]
                        },
                        {
                            "Id": 119,
                            "GroupName": "sss",
                            "ParentId": 57,
                            "ParentName": null,
                            "IsDefault": 0,
                            "AdminUserId": "sunnyyyli",
                            "UserList": null,
                            "Description": "",
                            "Location": 2,
                            "Children": null,
                            "HasChildren": false,
                            "ResourceList": [
                                {
                                    "ResourceName": "PageEdit",
                                    "ResourceValue": false,
                                    "CanChange": true,
                                    "Tips": ""
                                },
                                {
                                    "ResourceName": "PageRetrieval",
                                    "ResourceValue": false,
                                    "CanChange": true,
                                    "Tips": ""
                                },
                                {
                                    "ResourceName": "PageExport",
                                    "ResourceValue": false,
                                    "CanChange": true,
                                    "Tips": ""
                                },
                                {
                                    "ResourceName": "PageShareAndIframe",
                                    "ResourceValue": false,
                                    "CanChange": true,
                                    "Tips": ""
                                },
                                {
                                    "ResourceName": "PageView",
                                    "ResourceValue": false,
                                    "CanChange": true,
                                    "Tips": ""
                                }
                            ]
                        }
                    ],
                    "HasChildren": true,
                    "ResourceList": [
                        {
                            "ResourceName": "PageEdit",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageRetrieval",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageExport",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageShareAndIframe",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageView",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        }
                    ]
                },
                {
                    "Id": 72,
                    "GroupName": "最新用户层级",
                    "ParentId": -1,
                    "ParentName": null,
                    "IsDefault": 0,
                    "AdminUserId": "samjzhang",
                    "UserList": null,
                    "Description": null,
                    "Location": 11,
                    "Children": null,
                    "HasChildren": false,
                    "ResourceList": [
                        {
                            "ResourceName": "PageEdit",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageRetrieval",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageExport",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageShareAndIframe",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        },
                        {
                            "ResourceName": "PageView",
                            "ResourceValue": false,
                            "CanChange": true,
                            "Tips": ""
                        }
                    ]
                }
            ],
            "Total": 24,
            "TotalPages": 3
        }
    }
}
```

