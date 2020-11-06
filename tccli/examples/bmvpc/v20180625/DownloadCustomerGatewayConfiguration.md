**Example 1: 下载VPN通道配置**



Input: 

```
tccli bmvpc DownloadCustomerGatewayConfiguration --cli-unfold-argument  \
    --Version 2018-06-25 \
    --VpnConnectionId vpnx-5p7vkch8 \
    --VendorName h3c
```

Output: 
```
{
    "Response": {
        "CustomerGatewayConfiguration": "# VPC utilizes unique identifiers to manipulate the configuration of\r\n# a VPN Connection. Each VPN Connection is assigned an identifier and is\r\n# associated with Virtual Private Gateway ...",
        "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b"
    }
}
```

