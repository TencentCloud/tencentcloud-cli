**Example 1: 示例1**

示例1

Input: 

```
tccli csip DescribeListenerList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Domain": "www.testwaf0420.com,",
                "ListenerId": "lbl-5n1jiwjo",
                "ListenerName": "80",
                "LoadBalancerId": "lb-pflq0j2e",
                "LoadBalancerName": "lb-642137c1",
                "LoadBalancerType": "OPEN",
                "NumericalVpcId": 2783729,
                "Protocol": "HTTP",
                "Region": "gz",
                "VPort": 80,
                "Vip": "1.14.234.167",
                "Zone": "ap-guangzhou-6"
            },
            {
                "Domain": "1.15.159.154,,1.15.159.154,,1.15.159.154,,1.15.159.154,,1.15.159.154,,1.15.159.154,,1.15.159.154,,1.15.159.154,",
                "ListenerId": "lbl-gkydcakh",
                "ListenerName": "test-alert",
                "LoadBalancerId": "lb-bf5sfyqz",
                "LoadBalancerName": "autotest_HoneyPot",
                "LoadBalancerType": "OPEN",
                "NumericalVpcId": 3888171,
                "Protocol": "HTTP",
                "Region": "sh",
                "VPort": 8000,
                "Vip": "1.15.159.154",
                "Zone": "ap-shanghai-2"
            }
        ],
        "RequestId": "83be069d-0b57-40df-8faf-b3f7751d7eea",
        "Total": 2
    }
}
```

