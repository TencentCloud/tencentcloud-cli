**Example 1: 获取轮流值班**

获取轮流值班

Input: 

```
tccli wedata DescribeDutyScheduleDetails --cli-unfold-argument  \
    --Id 132 \
    --QueryDate 2023-12 \
    --Filters.0.Name SHIFT \
    --Filters.0.Values 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Day": "2023-12-21",
                "Duty": [
                    {
                        "DutyPersons": [
                            {
                                "OwnerUserId": "100028448903",
                                "TenantId": 1315051789,
                                "UserId": "100023475394",
                                "UserName": "andyylzhang"
                            }
                        ],
                        "DutyScheduleId": 3,
                        "EndTime": "20:00:00",
                        "StartTime": "08:00:00"
                    }
                ]
            },
            {
                "Day": "2023-12-20",
                "Duty": [
                    {
                        "DutyPersons": [
                            {
                                "OwnerUserId": "100028448903",
                                "TenantId": 1315051789,
                                "UserId": "100022459089",
                                "UserName": "plaguewang"
                            }
                        ],
                        "DutyScheduleId": 3,
                        "EndTime": "20:00:00",
                        "StartTime": "08:00:00"
                    }
                ]
            },
            {
                "Day": "2023-12-01",
                "Duty": [
                    {
                        "DutyPersons": [
                            {
                                "OwnerUserId": "100028448903",
                                "TenantId": 1315051789,
                                "UserId": "100023475394",
                                "UserName": "andyylzhang"
                            }
                        ],
                        "DutyScheduleId": 3,
                        "EndTime": "20:00:00",
                        "StartTime": "08:00:00"
                    }
                ]
            },
            {
                "Day": "2023-12-23",
                "Duty": [
                    {
                        "DutyPersons": [
                            {
                                "OwnerUserId": "100028448903",
                                "TenantId": 1315051789,
                                "UserId": "100023475394",
                                "UserName": "andyylzhang"
                            }
                        ],
                        "DutyScheduleId": 3,
                        "EndTime": "20:00:00",
                        "StartTime": "08:00:00"
                    }
                ]
            },
            {
                "Day": "2023-12-22",
                "Duty": [
                    {
                        "DutyPersons": [
                            {
                                "OwnerUserId": "100028448903",
                                "TenantId": 1315051789,
                                "UserId": "100022459089",
                                "UserName": "plaguewang"
                            }
                        ],
                        "DutyScheduleId": 3,
                        "EndTime": "20:00:00",
                        "StartTime": "08:00:00"
                    }
                ]
            },
            {
                "Day": "2023-12-14",
                "Duty": [
                    {
                        "DutyPersons": [
                            {
                                "OwnerUserId": "100028448903",
                                "TenantId": 1315051789,
                                "UserId": "100022459089",
                                "UserName": "plaguewang"
                            }
                        ],
                        "DutyScheduleId": 3,
                        "EndTime": "20:00:00",
                        "StartTime": "08:00:00"
                    }
                ]
            },
            {
                "Day": "2023-12-13",
                "Duty": [
                    {
                        "DutyPersons": [
                            {
                                "OwnerUserId": "100028448903",
                                "TenantId": 1315051789,
                                "UserId": "100023475394",
                                "UserName": "andyylzhang"
                            }
                        ],
                        "DutyScheduleId": 3,
                        "EndTime": "20:00:00",
                        "StartTime": "08:00:00"
                    }
                ]
            },
            {
                "Day": "2023-12-16",
                "Duty": [
                    {
                        "DutyPersons": [
                            {
                                "OwnerUserId": "100028448903",
                                "TenantId": 1315051789,
                                "UserId": "100022459089",
                                "UserName": "plaguewang"
                            }
                        ],
                        "DutyScheduleId": 3,
                        "EndTime": "20:00:00",
                        "StartTime": "08:00:00"
                    }
                ]
            },
            {
                "Day": "2023-12-15",
                "Duty": [
                    {
                        "DutyPersons": [
                            {
                                "OwnerUserId": "100028448903",
                                "TenantId": 1315051789,
                                "UserId": "100023475394",
                                "UserName": "andyylzhang"
                            }
                        ],
                        "DutyScheduleId": 3,
                        "EndTime": "20:00:00",
                        "StartTime": "08:00:00"
                    }
                ]
            },
            {
                "Day": "2023-12-18",
                "Duty": [
                    {
                        "DutyPersons": [
                            {
                                "OwnerUserId": "100028448903",
                                "TenantId": 1315051789,
                                "UserId": "100022459089",
                                "UserName": "plaguewang"
                            }
                        ],
                        "DutyScheduleId": 3,
                        "EndTime": "20:00:00",
                        "StartTime": "08:00:00"
                    }
                ]
            },
            {
                "Day": "2023-12-17",
                "Duty": [
                    {
                        "DutyPersons": [
                            {
                                "OwnerUserId": "100028448903",
                                "TenantId": 1315051789,
                                "UserId": "100023475394",
                                "UserName": "andyylzhang"
                            }
                        ],
                        "DutyScheduleId": 3,
                        "EndTime": "20:00:00",
                        "StartTime": "08:00:00"
                    }
                ]
            },
            {
                "Day": "2023-12-19",
                "Duty": [
                    {
                        "DutyPersons": [
                            {
                                "OwnerUserId": "100028448903",
                                "TenantId": 1315051789,
                                "UserId": "100023475394",
                                "UserName": "andyylzhang"
                            }
                        ],
                        "DutyScheduleId": 3,
                        "EndTime": "20:00:00",
                        "StartTime": "08:00:00"
                    }
                ]
            },
            {
                "Day": "2023-12-30",
                "Duty": [
                    {
                        "DutyPersons": [
                            {
                                "OwnerUserId": "100028448903",
                                "TenantId": 1315051789,
                                "UserId": "100022459089",
                                "UserName": "plaguewang"
                            }
                        ],
                        "DutyScheduleId": 3,
                        "EndTime": "20:00:00",
                        "StartTime": "08:00:00"
                    }
                ]
            },
            {
                "Day": "2023-12-10",
                "Duty": [
                    {
                        "DutyPersons": [
                            {
                                "OwnerUserId": "100028448903",
                                "TenantId": 1315051789,
                                "UserId": "100022459089",
                                "UserName": "plaguewang"
                            }
                        ],
                        "DutyScheduleId": 3,
                        "EndTime": "20:00:00",
                        "StartTime": "08:00:00"
                    }
                ]
            },
            {
                "Day": "2023-12-31",
                "Duty": [
                    {
                        "DutyPersons": [
                            {
                                "OwnerUserId": "100028448903",
                                "TenantId": 1315051789,
                                "UserId": "100023475394",
                                "UserName": "andyylzhang"
                            }
                        ],
                        "DutyScheduleId": 3,
                        "EndTime": "20:00:00",
                        "StartTime": "08:00:00"
                    }
                ]
            },
            {
                "Day": "2023-12-12",
                "Duty": [
                    {
                        "DutyPersons": [
                            {
                                "OwnerUserId": "100028448903",
                                "TenantId": 1315051789,
                                "UserId": "100022459089",
                                "UserName": "plaguewang"
                            }
                        ],
                        "DutyScheduleId": 3,
                        "EndTime": "20:00:00",
                        "StartTime": "08:00:00"
                    }
                ]
            },
            {
                "Day": "2023-12-11",
                "Duty": [
                    {
                        "DutyPersons": [
                            {
                                "OwnerUserId": "100028448903",
                                "TenantId": 1315051789,
                                "UserId": "100023475394",
                                "UserName": "andyylzhang"
                            }
                        ],
                        "DutyScheduleId": 3,
                        "EndTime": "20:00:00",
                        "StartTime": "08:00:00"
                    }
                ]
            },
            {
                "Day": "2023-12-03",
                "Duty": [
                    {
                        "DutyPersons": [
                            {
                                "OwnerUserId": "100028448903",
                                "TenantId": 1315051789,
                                "UserId": "100023475394",
                                "UserName": "andyylzhang"
                            }
                        ],
                        "DutyScheduleId": 3,
                        "EndTime": "20:00:00",
                        "StartTime": "08:00:00"
                    }
                ]
            },
            {
                "Day": "2023-12-25",
                "Duty": [
                    {
                        "DutyPersons": [
                            {
                                "OwnerUserId": "100028448903",
                                "TenantId": 1315051789,
                                "UserId": "100023475394",
                                "UserName": "andyylzhang"
                            }
                        ],
                        "DutyScheduleId": 3,
                        "EndTime": "20:00:00",
                        "StartTime": "08:00:00"
                    }
                ]
            },
            {
                "Day": "2023-12-02",
                "Duty": [
                    {
                        "DutyPersons": [
                            {
                                "OwnerUserId": "100028448903",
                                "TenantId": 1315051789,
                                "UserId": "100022459089",
                                "UserName": "plaguewang"
                            }
                        ],
                        "DutyScheduleId": 3,
                        "EndTime": "20:00:00",
                        "StartTime": "08:00:00"
                    }
                ]
            },
            {
                "Day": "2023-12-24",
                "Duty": [
                    {
                        "DutyPersons": [
                            {
                                "OwnerUserId": "100028448903",
                                "TenantId": 1315051789,
                                "UserId": "100022459089",
                                "UserName": "plaguewang"
                            }
                        ],
                        "DutyScheduleId": 3,
                        "EndTime": "20:00:00",
                        "StartTime": "08:00:00"
                    }
                ]
            },
            {
                "Day": "2023-12-05",
                "Duty": [
                    {
                        "DutyPersons": [
                            {
                                "OwnerUserId": "100028448903",
                                "TenantId": 1315051789,
                                "UserId": "100023475394",
                                "UserName": "andyylzhang"
                            }
                        ],
                        "DutyScheduleId": 3,
                        "EndTime": "20:00:00",
                        "StartTime": "08:00:00"
                    }
                ]
            },
            {
                "Day": "2023-12-27",
                "Duty": [
                    {
                        "DutyPersons": [
                            {
                                "OwnerUserId": "100028448903",
                                "TenantId": 1315051789,
                                "UserId": "100023475394",
                                "UserName": "andyylzhang"
                            }
                        ],
                        "DutyScheduleId": 3,
                        "EndTime": "20:00:00",
                        "StartTime": "08:00:00"
                    }
                ]
            },
            {
                "Day": "2023-12-04",
                "Duty": [
                    {
                        "DutyPersons": [
                            {
                                "OwnerUserId": "100028448903",
                                "TenantId": 1315051789,
                                "UserId": "100022459089",
                                "UserName": "plaguewang"
                            }
                        ],
                        "DutyScheduleId": 3,
                        "EndTime": "20:00:00",
                        "StartTime": "08:00:00"
                    }
                ]
            },
            {
                "Day": "2023-12-26",
                "Duty": [
                    {
                        "DutyPersons": [
                            {
                                "OwnerUserId": "100028448903",
                                "TenantId": 1315051789,
                                "UserId": "100022459089",
                                "UserName": "plaguewang"
                            }
                        ],
                        "DutyScheduleId": 3,
                        "EndTime": "20:00:00",
                        "StartTime": "08:00:00"
                    }
                ]
            },
            {
                "Day": "2023-12-07",
                "Duty": [
                    {
                        "DutyPersons": [
                            {
                                "OwnerUserId": "100028448903",
                                "TenantId": 1315051789,
                                "UserId": "100023475394",
                                "UserName": "andyylzhang"
                            }
                        ],
                        "DutyScheduleId": 3,
                        "EndTime": "20:00:00",
                        "StartTime": "08:00:00"
                    }
                ]
            },
            {
                "Day": "2023-12-29",
                "Duty": [
                    {
                        "DutyPersons": [
                            {
                                "OwnerUserId": "100028448903",
                                "TenantId": 1315051789,
                                "UserId": "100023475394",
                                "UserName": "andyylzhang"
                            }
                        ],
                        "DutyScheduleId": 3,
                        "EndTime": "20:00:00",
                        "StartTime": "08:00:00"
                    }
                ]
            },
            {
                "Day": "2023-12-06",
                "Duty": [
                    {
                        "DutyPersons": [
                            {
                                "OwnerUserId": "100028448903",
                                "TenantId": 1315051789,
                                "UserId": "100022459089",
                                "UserName": "plaguewang"
                            }
                        ],
                        "DutyScheduleId": 3,
                        "EndTime": "20:00:00",
                        "StartTime": "08:00:00"
                    }
                ]
            },
            {
                "Day": "2023-12-28",
                "Duty": [
                    {
                        "DutyPersons": [
                            {
                                "OwnerUserId": "100028448903",
                                "TenantId": 1315051789,
                                "UserId": "100022459089",
                                "UserName": "plaguewang"
                            }
                        ],
                        "DutyScheduleId": 3,
                        "EndTime": "20:00:00",
                        "StartTime": "08:00:00"
                    }
                ]
            },
            {
                "Day": "2023-12-09",
                "Duty": [
                    {
                        "DutyPersons": [
                            {
                                "OwnerUserId": "100028448903",
                                "TenantId": 1315051789,
                                "UserId": "100023475394",
                                "UserName": "andyylzhang"
                            }
                        ],
                        "DutyScheduleId": 3,
                        "EndTime": "20:00:00",
                        "StartTime": "08:00:00"
                    }
                ]
            },
            {
                "Day": "2023-12-08",
                "Duty": [
                    {
                        "DutyPersons": [
                            {
                                "OwnerUserId": "100028448903",
                                "TenantId": 1315051789,
                                "UserId": "100022459089",
                                "UserName": "plaguewang"
                            }
                        ],
                        "DutyScheduleId": 3,
                        "EndTime": "20:00:00",
                        "StartTime": "08:00:00"
                    }
                ]
            }
        ],
        "RequestId": "00327e43-fcf0-4241-8898-ddc6c4154a4b"
    }
}
```

**Example 2: 获取值班信息，日历格式**



Input: 

```
tccli wedata DescribeDutyScheduleDetails --cli-unfold-argument  \
    --QueryDate 2022-08 \
    --Id 2
```

Output: 
```
{
    "Response": {
        "RequestId": "cf860f2d-e60b-4232-bf22-b22d955cb7b3",
        "Data": [
            {
                "Day": "2022-08-12",
                "Duty": [
                    {
                        "DutyScheduleId": 2,
                        "StartTime": "00:00:00",
                        "EndTime": "12:59:59",
                        "DutyPersons": [
                            {
                                "OwnerUserId": "100019092402",
                                "UserId": "100019092402",
                                "TenantId": 11,
                                "UserName": "fletcherli"
                            }
                        ]
                    }
                ]
            },
            {
                "Day": "2022-08-11",
                "Duty": [
                    {
                        "DutyScheduleId": 2,
                        "StartTime": "00:00:00",
                        "EndTime": "12:59:59",
                        "DutyPersons": [
                            {
                                "OwnerUserId": "100019092402",
                                "UserId": "100019092402",
                                "TenantId": 11,
                                "UserName": "fletcherli"
                            }
                        ]
                    }
                ]
            },
            {
                "Day": "2022-08-10",
                "Duty": []
            },
            {
                "Day": "2022-08-31",
                "Duty": []
            },
            {
                "Day": "2022-08-30",
                "Duty": []
            },
            {
                "Day": "2022-08-19",
                "Duty": [
                    {
                        "DutyScheduleId": 2,
                        "StartTime": "00:00:00",
                        "EndTime": "12:59:59",
                        "DutyPersons": [
                            {
                                "OwnerUserId": "100019092402",
                                "UserId": "100019092402",
                                "TenantId": 11,
                                "UserName": "fletcherli"
                            }
                        ]
                    }
                ]
            },
            {
                "Day": "2022-08-18",
                "Duty": [
                    {
                        "DutyScheduleId": 2,
                        "StartTime": "00:00:00",
                        "EndTime": "12:59:59",
                        "DutyPersons": [
                            {
                                "OwnerUserId": "100019092402",
                                "UserId": "100019092402",
                                "TenantId": 11,
                                "UserName": "fletcherli"
                            }
                        ]
                    }
                ]
            },
            {
                "Day": "2022-08-17",
                "Duty": []
            },
            {
                "Day": "2022-08-16",
                "Duty": []
            },
            {
                "Day": "2022-08-15",
                "Duty": []
            },
            {
                "Day": "2022-08-14",
                "Duty": []
            },
            {
                "Day": "2022-08-13",
                "Duty": []
            },
            {
                "Day": "2022-08-01",
                "Duty": []
            },
            {
                "Day": "2022-08-23",
                "Duty": []
            },
            {
                "Day": "2022-08-22",
                "Duty": []
            },
            {
                "Day": "2022-08-21",
                "Duty": []
            },
            {
                "Day": "2022-08-20",
                "Duty": []
            },
            {
                "Day": "2022-08-09",
                "Duty": []
            },
            {
                "Day": "2022-08-08",
                "Duty": []
            },
            {
                "Day": "2022-08-07",
                "Duty": []
            },
            {
                "Day": "2022-08-29",
                "Duty": []
            },
            {
                "Day": "2022-08-06",
                "Duty": []
            },
            {
                "Day": "2022-08-28",
                "Duty": []
            },
            {
                "Day": "2022-08-05",
                "Duty": [
                    {
                        "DutyScheduleId": 2,
                        "StartTime": "00:00:00",
                        "EndTime": "12:59:59",
                        "DutyPersons": [
                            {
                                "OwnerUserId": "100019092402",
                                "UserId": "100019092402",
                                "TenantId": 11,
                                "UserName": "fletcherli"
                            }
                        ]
                    }
                ]
            },
            {
                "Day": "2022-08-27",
                "Duty": []
            },
            {
                "Day": "2022-08-04",
                "Duty": [
                    {
                        "DutyScheduleId": 2,
                        "StartTime": "00:00:00",
                        "EndTime": "12:59:59",
                        "DutyPersons": [
                            {
                                "OwnerUserId": "100019092402",
                                "UserId": "100019092402",
                                "TenantId": 11,
                                "UserName": "fletcherli"
                            }
                        ]
                    }
                ]
            },
            {
                "Day": "2022-08-26",
                "Duty": [
                    {
                        "DutyScheduleId": 2,
                        "StartTime": "00:00:00",
                        "EndTime": "12:59:59",
                        "DutyPersons": [
                            {
                                "OwnerUserId": "100019092402",
                                "UserId": "100019092402",
                                "TenantId": 11,
                                "UserName": "fletcherli"
                            }
                        ]
                    }
                ]
            },
            {
                "Day": "2022-08-03",
                "Duty": []
            },
            {
                "Day": "2022-08-25",
                "Duty": [
                    {
                        "DutyScheduleId": 2,
                        "StartTime": "00:00:00",
                        "EndTime": "12:59:59",
                        "DutyPersons": [
                            {
                                "OwnerUserId": "100019092402",
                                "UserId": "100019092402",
                                "TenantId": 11,
                                "UserName": "fletcherli"
                            }
                        ]
                    }
                ]
            },
            {
                "Day": "2022-08-02",
                "Duty": []
            },
            {
                "Day": "2022-08-24",
                "Duty": []
            }
        ]
    }
}
```

