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
                "Domain": "www.testwaf0420.com,,baidu.com,,baidu.com,,baidu.com,,www.testwaf0420.com,,rn.dzoyzy.top,,www.testwaf0420.com,,baidu.com,,www.testwaf0420.com,,baidu.com,",
                "ListenerId": "lbl-5n1jiwjo",
                "ListenerName": "80",
                "LoadBalancerDomain": "",
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
                "Domain": "81.71.21.14,,81.71.21.14,,81.71.21.14,,81.71.21.14,,81.71.21.14,,81.71.21.14,,81.71.21.14,,81.71.21.14,",
                "ListenerId": "lbl-c2tgl6w0",
                "ListenerName": "web",
                "LoadBalancerDomain": "",
                "LoadBalancerId": "lb-meckpdk0",
                "LoadBalancerName": "lsy",
                "LoadBalancerType": "OPEN",
                "NumericalVpcId": 8246908,
                "Protocol": "HTTP",
                "Region": "gz",
                "VPort": 80,
                "Vip": "81.71.21.14",
                "Zone": "ap-guangzhou-4"
            },
            {
                "Domain": "1.15.159.154,,1.15.159.154,,1.15.159.154,,1.15.159.154,,1.15.159.154,,1.15.159.154,,1.15.159.154,,1.15.159.154,",
                "ListenerId": "lbl-gkydcakh",
                "ListenerName": "test-alert",
                "LoadBalancerDomain": "",
                "LoadBalancerId": "lb-bf5sfyqz",
                "LoadBalancerName": "autotest_HoneyPot",
                "LoadBalancerType": "OPEN",
                "NumericalVpcId": 3888171,
                "Protocol": "HTTP",
                "Region": "sh",
                "VPort": 8000,
                "Vip": "1.15.159.154",
                "Zone": "ap-shanghai-2"
            },
            {
                "Domain": ",",
                "ListenerId": "lbl-mlrg4y76",
                "ListenerName": "test",
                "LoadBalancerDomain": "",
                "LoadBalancerId": "lb-pflq0j2e",
                "LoadBalancerName": "lb-642137c1",
                "LoadBalancerType": "OPEN",
                "NumericalVpcId": 2783729,
                "Protocol": "HTTP",
                "Region": "gz",
                "VPort": 8080,
                "Vip": "1.14.234.167",
                "Zone": "ap-guangzhou-6"
            }
        ],
        "RequestId": "3f2d43d2-e003-4872-8953-18d080e98c1d",
        "Total": 4
    }
}
```

