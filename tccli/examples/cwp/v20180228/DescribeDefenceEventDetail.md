**Example 1: 获取漏洞防御事件详情**



Input: 

```
tccli cwp DescribeDefenceEventDetail --cli-unfold-argument  \
    --Id 123
```

Output: 
```
{
    "Response": {
        "Data": {
            "Id": 10001,
            "Status": 1,
            "Quuid": "05f0bcab-726c-4ea4-8109-bcd03d5598f7",
            "Alias": "Alias-name",
            "MachineStatus": "ONLINE",
            "PrivateIp": "1.1.1.1",
            "PublicIp": "1.1.1.1.",
            "CreateTime": "2024-10-23 11:41:10",
            "MergeTime": "2024-10-23 11:43:52",
            "VulName": "Apache log4j2 远程代码执行漏洞 (CVE-2021-44228)",
            "EventType": 2,
            "Count": 20,
            "CveId": "CVE-2021-44228",
            "SourceIp": "",
            "City": "",
            "SourcePort": null,
            "Description": "腾讯安全注意到，一个Apache Log4j2高危漏洞细节已被公开，Log4j-2<2.15.0的版本中存在JNDI注入漏洞，当程序将用户输入的数据进行日志记录时，即可触发此漏洞，成功利用此漏洞可以在目标服务器上执行任意代码。",
            "Fix": "请注意，只有 log4j-core JAR 文件受此漏洞影响。仅使用 log4j-api JAR 文件而不使用 log4j-core JAR 文件的应用程序不受此漏洞的影响。腾讯安全专家建议受影响的用户尽快升级到2.16.0及以上版本。\n最新安全版本请参考官方安全通告：https://logging.apache.org/log4j/2.x/security.html\n更新包下载地址：https://logging.apache.org/log4j/2.x/download.html\n漏洞缓解措施 (仍会检出漏洞）：\n（1）从类路径中删除 JndiLookup 类： zip -q -d log4j-core-*.jar org/apache/logging/log4j/core/lookup/JndiLookup.class\n腾讯云WAF和云防火墙均已支持该漏洞防护\nWAF试用：https://cloud.tencent.com/act/pro/clbwafenterprise  \n配置WAF： https://console.cloud.tencent.com/guanjia/tea-instance-new\n云防火墙试用：https://console.cloud.tencent.com/cfw/ips",
            "NetworkPayload": "OiAK",
            "Pid": 20545,
            "MainClass": "org.eclipse.jetty.start.Main",
            "StackTrace": "org.apache.logging.log4j.core.lookup.JndiLookup.lookup\norg.apache.logging.log4j.core.lookup.Interpolator.lookup\norg.apache.logging.log4j.core.lookup.StrSubstitutor.resolveVariable\norg.apache.logging.log4j.core.lookup.StrSubstitutor.substitute\norg.apache.logging.log4j.core.lookup.StrSubstitutor.substitute\norg.apache.logging.log4j.core.lookup.StrSubstitutor.replace\norg.apache.logging.log4j.core.pattern.MessagePatternConverter.format\norg.apache.logging.log4j.core.pattern.PatternFormatter.format\norg.apache.logging.log4j.core.pattern.MaxLengthConverter.format\norg.apache.logging.log4j.core.pattern.PatternFormatter.format\norg.apache.logging.log4j.core.layout.PatternLayout$PatternSerializer.toSerializable\norg.apache.logging.log4j.core.layout.PatternLayout.toText\norg.apache.logging.log4j.core.layout.PatternLayout.encode\norg.apache.logging.log4j.core.layout.PatternLayout.encode\norg.apache.logging.log4j.core.appender.AbstractOutputStreamAppender.directEncodeEvent\norg.apache.logging.log4j.core.appender.AbstractOutputStreamAppender.tryAppend\norg.apache.logging.log4j.core.appender.AbstractOutputStreamAppender.append\norg.apache.logging.log4j.core.config.AppenderControl.tryCallAppender\norg.apache.logging.log4j.core.config.AppenderControl.callAppender0\norg.apache.logging.log4j.core.config.AppenderControl.callAppenderPreventRecursion\norg.apache.logging.log4j.core.config.AppenderControl.callAppender\norg.apache.logging.log4j.core.config.LoggerConfig.callAppenders\norg.apache.logging.log4j.core.async.AsyncLoggerConfig.callAppenders\norg.apache.logging.log4j.core.config.LoggerConfig.processLogEvent\norg.apache.logging.log4j.core.config.LoggerConfig.log\norg.apache.logging.log4j.core.async.AsyncLoggerConfig.log\norg.apache.logging.log4j.core.async.AsyncLoggerConfig.logToAsyncLoggerConfigsOnCurrentThread\norg.apache.logging.log4j.core.async.AsyncLoggerConfigDisruptor$Log4jEventWrapperHandler.onEvent\norg.apache.logging.log4j.core.async.AsyncLoggerConfigDisruptor$Log4jEventWrapperHandler.onEvent\ncom.lmax.disruptor.BatchEventProcessor.processEvents\ncom.lmax.disruptor.BatchEventProcessor.run\njava.lang.Thread.run\n",
            "EventDetail": "[{\"name\":\"jndiurl\",\"value\":\"ldap://1.8.0_102.example.com\"}]",
            "ExceptionPstree": "",
            "MachineExtraInfo": {
                "WanIP": "1.1.1.1",
                "PrivateIP": "1.1.1.1",
                "NetworkType": 1,
                "NetworkName": "vpc-12332112",
                "InstanceID": "ins-12332112",
                "HostName": "机器名称"
            }
        },
        "RequestId": "be6f6eec-0825-4e67-ab9a-c8568bbf736c"
    }
}
```

