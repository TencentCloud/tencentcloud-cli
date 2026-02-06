**Example 1: 查询NAT开关列表**

查询NAT开关列表

Input: 

```
tccli cfw DescribeNatFwSwitch --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Abnormal": 0,
                "CvmNum": 1,
                "Enable": 1,
                "Id": 33781,
                "NatId": "",
                "NatInsId": "cfwnat-84d3440f",
                "NatInsName": "[autotest][勿删]自动化测试",
                "NatName": "",
                "Region": "ap-shanghai",
                "RouteId": "rtb-f5wqfibn",
                "RouteName": "default_copy_for_cfw",
                "Status": 0,
                "SubnetCidr": "10.8.2.0/24",
                "SubnetId": "subnet-j9cyo89p",
                "SubnetName": "[autotest][勿删]自动化测试C2",
                "VpcId": "vpc-d0t6wgo2",
                "VpcName": "[autotest][勿删]自动化测试C"
            },
            {
                "Abnormal": 0,
                "CvmNum": 0,
                "Enable": 1,
                "Id": 34636,
                "NatId": "",
                "NatInsId": "cfwnat-84d3440f",
                "NatInsName": "[autotest][勿删]自动化测试",
                "NatName": "",
                "Region": "ap-shanghai",
                "RouteId": "rtb-l28qa73d",
                "RouteName": "default",
                "Status": 0,
                "SubnetCidr": "10.8.0.32/29",
                "SubnetId": "subnet-rsun76k7",
                "SubnetName": "防火墙专用子网_请勿删改",
                "VpcId": "vpc-d0t6wgo2",
                "VpcName": "[autotest][勿删]自动化测试C"
            },
            {
                "Abnormal": 0,
                "CvmNum": 0,
                "Enable": 1,
                "Id": 33779,
                "NatId": "",
                "NatInsId": "cfwnat-84d3440f",
                "NatInsName": "[autotest][勿删]自动化测试",
                "NatName": "",
                "Region": "ap-shanghai",
                "RouteId": "rtb-l28qa73d",
                "RouteName": "default",
                "Status": 0,
                "SubnetCidr": "10.8.3.0/24",
                "SubnetId": "subnet-nem8hqnp",
                "SubnetName": "MYSQL",
                "VpcId": "vpc-d0t6wgo2",
                "VpcName": "[autotest][勿删]自动化测试C"
            },
            {
                "Abnormal": 0,
                "CvmNum": 1,
                "Enable": 1,
                "Id": 33780,
                "NatId": "",
                "NatInsId": "cfwnat-84d3440f",
                "NatInsName": "[autotest][勿删]自动化测试",
                "NatName": "",
                "Region": "ap-shanghai",
                "RouteId": "rtb-l28qa73d",
                "RouteName": "default",
                "Status": 0,
                "SubnetCidr": "10.8.1.0/24",
                "SubnetId": "subnet-jy2eionr",
                "SubnetName": "[autotest][勿删]自动化测试C1",
                "VpcId": "vpc-d0t6wgo2",
                "VpcName": "[autotest][勿删]自动化测试C"
            },
            {
                "Abnormal": 0,
                "CvmNum": 0,
                "Enable": 0,
                "Id": 34637,
                "NatId": "",
                "NatInsId": "cfwnat-7e170f6b",
                "NatInsName": "test",
                "NatName": "",
                "Region": "ap-beijing",
                "RouteId": "rtb-o18lgl2l",
                "RouteName": "default",
                "Status": 0,
                "SubnetCidr": "10.0.0.0/24",
                "SubnetId": "subnet-s1c8r185",
                "SubnetName": "nat防火墙临时测试",
                "VpcId": "vpc-0iz7ii4s",
                "VpcName": "nat防火墙临时测试"
            },
            {
                "Abnormal": 0,
                "CvmNum": 0,
                "Enable": 1,
                "Id": 34629,
                "NatId": "nat-de74cic7",
                "NatInsId": "cfwnat-01debc37",
                "NatInsName": "111",
                "NatName": "test1",
                "Region": "ap-shanghai",
                "RouteId": "rtb-pslbu0gx",
                "RouteName": "default",
                "Status": 0,
                "SubnetCidr": "172.20.0.0/24",
                "SubnetId": "subnet-8jm78x87",
                "SubnetName": "subnet1",
                "VpcId": "vpc-fmprtmz2",
                "VpcName": "dora1"
            },
            {
                "Abnormal": 0,
                "CvmNum": 0,
                "Enable": 0,
                "Id": 34633,
                "NatId": "nat-56jjs6mo",
                "NatInsId": "cfwnat-49f38b8b",
                "NatInsName": "测试接入",
                "NatName": "gltest",
                "Region": "ap-guangzhou",
                "RouteId": "rtb-pwcv5gaw",
                "RouteName": "default",
                "Status": 0,
                "SubnetCidr": "10.10.0.0/24",
                "SubnetId": "subnet-7z6dhany",
                "SubnetName": "fengqqiansub",
                "VpcId": "vpc-0nduhuff",
                "VpcName": "fengqqian-串行"
            }
        ],
        "FailData": [],
        "NatList": [
            {
                "Id": "nat-56jjs6mo",
                "Name": "gltest"
            },
            {
                "Id": "nat-de74cic7",
                "Name": "test1"
            }
        ],
        "OffNum": 2,
        "OnNum": 5,
        "RequestId": "2c74b129-10ea-434a-8e02-b125b9c3236b",
        "RouteList": [
            {
                "Id": "rtb-f5wqfibn",
                "Name": "default_copy_for_cfw"
            },
            {
                "Id": "rtb-l28qa73d",
                "Name": "default"
            },
            {
                "Id": "rtb-o18lgl2l",
                "Name": "default"
            },
            {
                "Id": "rtb-pslbu0gx",
                "Name": "default"
            },
            {
                "Id": "rtb-pwcv5gaw",
                "Name": "default"
            }
        ],
        "Total": 7,
        "VpcList": [
            {
                "Id": "vpc-0iz7ii4s",
                "Name": "nat防火墙临时测试"
            },
            {
                "Id": "vpc-0nduhuff",
                "Name": "fengqqian-串行"
            },
            {
                "Id": "vpc-d0t6wgo2",
                "Name": "[autotest][勿删]自动化测试C"
            },
            {
                "Id": "vpc-fmprtmz2",
                "Name": "dora1"
            }
        ]
    }
}
```

