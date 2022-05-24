**Example 1: 查询访问权限列表**



Input: 

```
tccli dasb DescribeAcls --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AclSet": [
            {
                "UserGroupSet": [
                    {
                        "Id": 1,
                        "Name": "xx"
                    }
                ],
                "AllowClipTextDown": true,
                "AllowShellFileDown": true,
                "AllowShellFileUp": true,
                "ValidateFrom": "2020-09-22T00:00:00+00:00",
                "AllowDiskFileDown": true,
                "UserSet": [
                    {
                        "UserName": "xx",
                        "AuthType": 1,
                        "ValidateTo": "2020-09-22T00:00:00+00:00",
                        "RealName": "xx",
                        "Email": "xx",
                        "Phone": "xx",
                        "GroupSet": [
                            {
                                "Id": 1,
                                "Name": "xx"
                            }
                        ],
                        "ValidateFrom": "2020-09-22T00:00:00+00:00",
                        "Id": 1
                    }
                ],
                "AllowFileUp": true,
                "Status": 1,
                "ValidateTo": "2020-09-22T00:00:00+00:00",
                "DeviceSet": [
                    {
                        "Kind": 1,
                        "GroupSet": [
                            {
                                "Id": 1,
                                "Name": "xx"
                            }
                        ],
                        "Resource": {
                            "RenewFlag": 1,
                            "Zone": "xx",
                            "SubnetName": "xx",
                            "Nodes": 1,
                            "Status": 1,
                            "VpcId": "xx",
                            "SubProductCode": "xx",
                            "ResourceId": "xx",
                            "VpcName": "xx",
                            "ApCode": "xx",
                            "SubnetId": "xx",
                            "ResourceName": "xx",
                            "Expired": true,
                            "Deployed": true,
                            "ProductCode": "xx",
                            "PublicIpSet": [
                                "xx"
                            ],
                            "PrivateIpSet": [
                                "xx"
                            ],
                            "Pid": 1,
                            "VpcCidrBlock": "xx",
                            "ExpireTime": "2020-09-22T00:00:00+00:00",
                            "SvArgs": "xx",
                            "CidrBlock": "xx",
                            "CreateTime": "2020-09-22T00:00:00+00:00"
                        },
                        "Name": "xx",
                        "InstanceId": "xx",
                        "OsName": "xx",
                        "AccountCount": 1,
                        "PrivateIp": "xx",
                        "PublicIp": "xx",
                        "VpcId": "xx",
                        "ApCode": "xx",
                        "SubnetId": "xx",
                        "Port": 1,
                        "Id": 1
                    }
                ],
                "AllowDiskRedirect": false,
                "AllowAnyAccount": true,
                "MaxFileDownSize": 1,
                "Name": "xx",
                "AllowDiskFileUp": true,
                "AllowClipFileUp": false,
                "AllowClipTextUp": true,
                "AllowFileDown": true,
                "DeviceGroupSet": [
                    {
                        "Id": 1,
                        "Name": "xx"
                    }
                ],
                "CmdTemplateSet": [
                    {
                        "CmdList": "xx",
                        "Name": "xx",
                        "Id": 1
                    }
                ],
                "AccountSet": [
                    "xx"
                ],
                "AllowClipFileDown": false,
                "MaxFileUpSize": 1,
                "Id": 1,
                "AllowFileDel": true
            }
        ],
        "RequestId": "xx"
    }
}
```

**Example 2: 根据用户和主机查询对应的权限**

根据用户和主机查询对应的权限

Input: 

```
tccli dasb DescribeAcls --cli-unfold-argument  \
    --AuthorizedUserIdSet 1 7 8 238 \
    --AuthorizedDeviceIdSet 63 64 82 100
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AclSet": [
            {
                "UserGroupSet": [
                    {
                        "Id": 1,
                        "Name": "xx"
                    }
                ],
                "AllowClipTextDown": true,
                "AllowShellFileDown": true,
                "AllowShellFileUp": true,
                "ValidateFrom": "2020-09-22T00:00:00+00:00",
                "AllowDiskFileDown": true,
                "UserSet": [
                    {
                        "UserName": "xx",
                        "AuthType": 1,
                        "ValidateTo": "2020-09-22T00:00:00+00:00",
                        "RealName": "xx",
                        "Email": "xx",
                        "Phone": "xx",
                        "GroupSet": [
                            {
                                "Id": 1,
                                "Name": "xx"
                            }
                        ],
                        "ValidateFrom": "2020-09-22T00:00:00+00:00",
                        "Id": 1
                    }
                ],
                "AllowFileUp": true,
                "Status": 1,
                "ValidateTo": "2020-09-22T00:00:00+00:00",
                "DeviceSet": [
                    {
                        "Kind": 1,
                        "GroupSet": [
                            {
                                "Id": 1,
                                "Name": "xx"
                            }
                        ],
                        "Resource": {
                            "RenewFlag": 1,
                            "Zone": "xx",
                            "SubnetName": "xx",
                            "Nodes": 1,
                            "Status": 1,
                            "VpcId": "xx",
                            "SubProductCode": "xx",
                            "ResourceId": "xx",
                            "VpcName": "xx",
                            "ApCode": "xx",
                            "SubnetId": "xx",
                            "ResourceName": "xx",
                            "Expired": true,
                            "Deployed": true,
                            "ProductCode": "xx",
                            "PublicIpSet": [
                                "xx"
                            ],
                            "PrivateIpSet": [
                                "xx"
                            ],
                            "Pid": 1,
                            "VpcCidrBlock": "xx",
                            "ExpireTime": "2020-09-22T00:00:00+00:00",
                            "SvArgs": "xx",
                            "CidrBlock": "xx",
                            "CreateTime": "2020-09-22T00:00:00+00:00"
                        },
                        "Name": "xx",
                        "InstanceId": "xx",
                        "OsName": "xx",
                        "AccountCount": 1,
                        "PrivateIp": "xx",
                        "PublicIp": "xx",
                        "VpcId": "xx",
                        "ApCode": "xx",
                        "SubnetId": "xx",
                        "Port": 1,
                        "Id": 1
                    }
                ],
                "AllowDiskRedirect": false,
                "AllowAnyAccount": true,
                "MaxFileDownSize": 1,
                "Name": "xx",
                "AllowDiskFileUp": true,
                "AllowClipFileUp": false,
                "AllowClipTextUp": true,
                "AllowFileDown": true,
                "DeviceGroupSet": [
                    {
                        "Id": 1,
                        "Name": "xx"
                    }
                ],
                "CmdTemplateSet": [
                    {
                        "CmdList": "xx",
                        "Name": "xx",
                        "Id": 1
                    }
                ],
                "AccountSet": [
                    "xx"
                ],
                "AllowClipFileDown": false,
                "MaxFileUpSize": 1,
                "Id": 1,
                "AllowFileDel": true
            }
        ],
        "RequestId": "xx"
    }
}
```

