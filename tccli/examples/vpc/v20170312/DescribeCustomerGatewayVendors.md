**Example 1: 查询可支持的对端网关厂商信息**

本接口（DescribeCustomerGatewayVendors）用于查询可支持的对端网关厂商信息。

Input: 

```
tccli vpc DescribeCustomerGatewayVendors --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "CustomerGatewayVendorSet": [
            {
                "Platform": "ios",
                "SoftwareVersion": "V15.4",
                "VendorName": "cisco"
            },
            {
                "Platform": "comware",
                "SoftwareVersion": "V1.0",
                "VendorName": "h3c"
            }
        ],
        "RequestId": "ccda8bff-d7aa-4a16-8a72-13e72a116205"
    }
}
```

