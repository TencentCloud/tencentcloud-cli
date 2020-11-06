**Example 1: Downloading a VPN tunnel configuration**



Input: 

```
tccli vpc DownloadCustomerGatewayConfiguration --cli-unfold-argument  \
    --Version 2017-03-12 \
    --VpnGatewayId vpngw-p4lmqawn \
    --VpnConnectionId vpnx-5p7vkch8 \
    --CustomerGatewayVendor.Platform comware \
    --CustomerGatewayVendor.SoftwareVersion V1.0 \
    --CustomerGatewayVendor.VendorName h3c \
    --InterfaceName eth0
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

