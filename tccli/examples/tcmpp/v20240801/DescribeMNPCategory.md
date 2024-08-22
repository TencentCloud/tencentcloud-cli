**Example 1: DescribeMNPCategory**



Input: 

```
tccli tcmpp DescribeMNPCategory --cli-unfold-argument  \
    --PlatformId T04257DS9431720WTAG
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "TypeId": 10000,
                "TypeName": "Logistics Services",
                "CreateTime": 1719991302,
                "CreateUser": "admin",
                "IsSystem": true,
                "TypeValue": [
                    "1_Pickup/Delivery",
                    "2_Search",
                    "10_Postal Service",
                    "11_Loading and unloading",
                    "12_Warehousing",
                    "13_Express Locker",
                    "14_Cargo Transportation"
                ]
            },
            {
                "TypeId": 10001,
                "TypeName": "Education Services",
                "CreateTime": 1719991302,
                "CreateUser": "admin",
                "IsSystem": true,
                "TypeValue": [
                    "4_Driving School Training",
                    "15_Academic Education (Training Institutions)",
                    "16_Academic Education (Schools)",
                    "18_Driving School Platform",
                    "19_Education Platform",
                    "20_Quality Education",
                    "21_Infant and Toddler Education",
                    "22_Educational Equipment",
                    "23_Study Abroad",
                    "24_Special Populations Education",
                    "25_Online Video Courses",
                    "307_Online Education"
                ]
            }
        ],
        "RequestId": "d1d8f191-f4a4-4f72-a358-1634f13bd1e1"
    }
}
```

