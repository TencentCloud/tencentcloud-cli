**Example 1: 查询API详情**



Input: 

```
tccli tsf DescribeApiDetail --cli-unfold-argument  \
    --MicroserviceId ms-2vzprpyp \
    --Path /facade/supplier/test \
    --Method POST \
    --ApplicationId application-gvkw2ejv \
    --PkgVersion jenkins-prod-supplier-1
```

Output: 
```
{
    "Response": {
        "RequestId": "b8427f00-c974-47b1-9827-978cdb043b9d",
        "Result": {
            "Request": [
                {
                    "Name": "supplierId",
                    "Type": "string",
                    "Description": "supplierId",
                    "Required": true,
                    "In": "query"
                }
            ],
            "Response": [
                {
                    "Name": "Res«Supplier»",
                    "Type": "#/Definitions/Res«Supplier»",
                    "Description": "OK"
                }
            ],
            "Definitions": [
                {
                    "Name": "Supplier",
                    "Properties": [
                        {
                            "Name": "abbrName",
                            "Type": "string"
                        },
                        {
                            "Name": "coordinatesSystem",
                            "Type": "integer(int32)"
                        },
                        {
                            "Name": "createTime",
                            "Type": "string(date-time)"
                        },
                        {
                            "Name": "id",
                            "Type": "string"
                        },
                        {
                            "Name": "invoiceLineNum",
                            "Type": "integer(int32)"
                        },
                        {
                            "Name": "invoiceMaxFee",
                            "Type": "integer(int64)"
                        },
                        {
                            "Name": "invoiceMinFee",
                            "Type": "integer(int64)"
                        },
                        {
                            "Name": "invoiceType",
                            "Type": "integer(int32)"
                        },
                        {
                            "Name": "isActive",
                            "Type": "integer(int32)"
                        },
                        {
                            "Name": "isTripEnable",
                            "Type": "integer(int32)"
                        },
                        {
                            "Name": "logo",
                            "Type": "string"
                        },
                        {
                            "Name": "name",
                            "Type": "string"
                        },
                        {
                            "Name": "priceRuleUrl",
                            "Type": "string"
                        },
                        {
                            "Name": "servicePhone",
                            "Type": "string"
                        },
                        {
                            "Name": "signKey",
                            "Type": "string"
                        },
                        {
                            "Name": "updateTime",
                            "Type": "string(date-time)"
                        }
                    ]
                },
                {
                    "Name": "Res«Supplier»",
                    "Properties": [
                        {
                            "Name": "code",
                            "Type": "integer(int32)"
                        },
                        {
                            "Name": "data",
                            "Type": "#/Definitions/Supplier"
                        },
                        {
                            "Name": "errmsg",
                            "Type": "string"
                        },
                        {
                            "Name": "success",
                            "Type": "boolean"
                        }
                    ]
                }
            ]
        }
    }
}
```

