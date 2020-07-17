# -*- coding: utf-8 -*-
DESC = "dayu-2018-07-09"
INFO = {
  "ModifyCCIpAllowDeny": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "Method",
        "desc": "add表示添加，delete表示删除"
      },
      {
        "name": "Type",
        "desc": "黑/白名单类型；取值[white(白名单)，black(黑名单)]"
      },
      {
        "name": "IpList",
        "desc": "黑/白名单的IP数组"
      },
      {
        "name": "Protocol",
        "desc": "可选字段，代表CC防护类型，取值[http（HTTP协议的CC防护），https（HTTPS协议的CC防护）]；当不填时，默认为HTTP协议的CC防护；当填写https时还需要填写Domain和RuleId字段；"
      },
      {
        "name": "Domain",
        "desc": "可选字段，表示HTTPS协议的7层转发规则域名（通过获取7层转发规则接口可以获取域名），只有当Protocol字段为https时才必须填写此字段；"
      },
      {
        "name": "RuleId",
        "desc": "可选字段，表示HTTPS协议的7层转发规则ID（通过获取7层转发规则接口可以获取规则ID），\n当Method为delete时，不用填写此字段；"
      }
    ],
    "desc": "添加或删除CC的IP黑白名单"
  },
  "DescribeDDoSCount": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "Ip",
        "desc": "资源的IP"
      },
      {
        "name": "StartTime",
        "desc": "统计开始时间"
      },
      {
        "name": "EndTime",
        "desc": "统计结束时间"
      },
      {
        "name": "MetricName",
        "desc": "指标，取值[traffic（攻击协议流量, 单位KB）, pkg（攻击协议报文数）, classnum（攻击事件次数）]"
      }
    ],
    "desc": "获取DDoS攻击占比分析"
  },
  "DeleteNewL4Rules": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP）"
      },
      {
        "name": "Rule",
        "desc": "删除接口结构体"
      }
    ],
    "desc": "删除L4转发规则"
  },
  "DescribeRuleSets": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）"
      },
      {
        "name": "IdList",
        "desc": "资源ID列表"
      }
    ],
    "desc": "获取资源的规则数"
  },
  "CreateNewL7RulesUpload": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP）"
      },
      {
        "name": "IdList",
        "desc": "资源ID列表"
      },
      {
        "name": "VipList",
        "desc": "资源IP列表"
      },
      {
        "name": "Rules",
        "desc": "规则列表"
      }
    ],
    "desc": "批量上传7层转发规则"
  },
  "CreateL7CCRule": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "Method",
        "desc": "操作码，取值[query(表示查询)，add(表示添加)，del(表示删除)]"
      },
      {
        "name": "RuleId",
        "desc": "7层转发规则ID，例如：rule-0000001"
      },
      {
        "name": "RuleConfig",
        "desc": "7层CC自定义规则参数，当操作码为query时，可以不用填写；当操作码为add或del时，必须填写，且数组长度只能为1；"
      }
    ],
    "desc": "此接口是7层CC的访问频控自定义规则（IP+Host维度，不支持具体的URI），此接口已弃用，请调用新接口CreateCCFrequencyRules，新接口同时支持IP+Host维度以及具体的URI；"
  },
  "CreateCCSelfDefinePolicy": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "Policy",
        "desc": "CC策略描述"
      }
    ],
    "desc": "创建CC自定义策略"
  },
  "DescribleL7Rules": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "RuleIdList",
        "desc": "规则ID，可选参数，填写后获取指定的规则"
      },
      {
        "name": "Limit",
        "desc": "一页条数，填0表示不分页"
      },
      {
        "name": "Offset",
        "desc": "页起始偏移，取值为(页码-1)*一页条数"
      },
      {
        "name": "Domain",
        "desc": "域名搜索，选填，当需要搜索域名请填写"
      },
      {
        "name": "ProtocolList",
        "desc": "转发协议搜索，选填，取值[http, https, http/https]"
      },
      {
        "name": "StatusList",
        "desc": "状态搜索，选填，取值[0(规则配置成功)，1(规则配置生效中)，2(规则配置失败)，3(规则删除生效中)，5(规则删除失败)，6(规则等待配置)，7(规则等待删除)，8(规则待配置证书)]"
      }
    ],
    "desc": "获取七层转发规则"
  },
  "ModifyResBindDDoSPolicy": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "PolicyId",
        "desc": "策略ID"
      },
      {
        "name": "Method",
        "desc": "绑定或解绑，bind表示绑定策略，unbind表示解绑策略"
      }
    ],
    "desc": "资源实例绑定DDoS高级策略"
  },
  "DescribeNewL7RulesErrHealth": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP)"
      },
      {
        "name": "RuleIdList",
        "desc": "规则Id列表"
      }
    ],
    "desc": "获取L7转发规则健康检查异常结果"
  },
  "CreateDDoSPolicyCase": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）"
      },
      {
        "name": "CaseName",
        "desc": "策略场景名，字符串长度小于64"
      },
      {
        "name": "PlatformTypes",
        "desc": "开发平台，取值[PC（PC客户端）， MOBILE（移动端）， TV（电视端）， SERVER（主机）]"
      },
      {
        "name": "AppType",
        "desc": "细分品类，取值[WEB（网站）， GAME（游戏）， APP（应用）， OTHER（其他）]"
      },
      {
        "name": "AppProtocols",
        "desc": "应用协议，取值[tcp（TCP协议），udp（UDP协议），icmp（ICMP协议），all（其他协议）]"
      },
      {
        "name": "TcpSportStart",
        "desc": "TCP业务起始端口，取值(0, 65535]"
      },
      {
        "name": "TcpSportEnd",
        "desc": "TCP业务结束端口，取值(0, 65535]，必须大于等于TCP业务起始端口"
      },
      {
        "name": "UdpSportStart",
        "desc": "UDP业务起始端口，取值范围(0, 65535]"
      },
      {
        "name": "UdpSportEnd",
        "desc": "UDP业务结束端口，取值范围(0, 65535)，必须大于等于UDP业务起始端口"
      },
      {
        "name": "HasAbroad",
        "desc": "是否有海外客户，取值[no（没有）, yes（有）]"
      },
      {
        "name": "HasInitiateTcp",
        "desc": "是否会主动对外发起TCP请求，取值[no（不会）, yes（会）]"
      },
      {
        "name": "HasInitiateUdp",
        "desc": "是否会主动对外发起UDP业务请求，取值[no（不会）, yes（会）]"
      },
      {
        "name": "PeerTcpPort",
        "desc": "主动发起TCP请求的端口，取值范围(0, 65535]"
      },
      {
        "name": "PeerUdpPort",
        "desc": "主动发起UDP请求的端口，取值范围(0, 65535]"
      },
      {
        "name": "TcpFootprint",
        "desc": "TCP载荷的固定特征码，字符串长度小于512"
      },
      {
        "name": "UdpFootprint",
        "desc": "UDP载荷的固定特征码，字符串长度小于512"
      },
      {
        "name": "WebApiUrl",
        "desc": "Web业务的API的URL"
      },
      {
        "name": "MinTcpPackageLen",
        "desc": "TCP业务报文长度最小值，取值范围(0, 1500)"
      },
      {
        "name": "MaxTcpPackageLen",
        "desc": "TCP业务报文长度最大值，取值范围(0, 1500)，必须大于等于TCP业务报文长度最小值"
      },
      {
        "name": "MinUdpPackageLen",
        "desc": "UDP业务报文长度最小值，取值范围(0, 1500)"
      },
      {
        "name": "MaxUdpPackageLen",
        "desc": "UDP业务报文长度最大值，取值范围(0, 1500)，必须大于等于UDP业务报文长度最小值"
      },
      {
        "name": "HasVPN",
        "desc": "是否有VPN业务，取值[no（没有）, yes（有）]"
      },
      {
        "name": "TcpPortList",
        "desc": "TCP业务端口列表，同时支持单个端口和端口段，字符串格式，例如：80,443,700-800,53,1000-3000"
      },
      {
        "name": "UdpPortList",
        "desc": "UDP业务端口列表，同时支持单个端口和端口段，字符串格式，例如：80,443,700-800,53,1000-3000"
      }
    ],
    "desc": "添加策略场景"
  },
  "DescribeDDoSNetTrend": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "MetricName",
        "desc": "指标，取值[bps(攻击流量带宽，pps(攻击包速率))]"
      },
      {
        "name": "Period",
        "desc": "统计粒度，取值[300(5分钟)，3600(小时)，86400(天)]"
      },
      {
        "name": "StartTime",
        "desc": "统计开始时间"
      },
      {
        "name": "EndTime",
        "desc": "统计结束时间"
      }
    ],
    "desc": "获取高防IP专业版资源的DDoS攻击指标数据"
  },
  "ModifyDDoSPolicyName": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）"
      },
      {
        "name": "PolicyId",
        "desc": "策略ID"
      },
      {
        "name": "Name",
        "desc": "策略名称"
      }
    ],
    "desc": "修改DDoS高级策略名称"
  },
  "ModifyL4Health": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "Healths",
        "desc": "健康检查参数数组"
      }
    ],
    "desc": "修改L4转发规则健康检查参数，支持的子产品：高防IP、高防IP专业版"
  },
  "DescribeDDoSUsedStatis": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP）"
      }
    ],
    "desc": "统计用户的高防资源的使用天数和DDoS攻击防护次数"
  },
  "DescribeDDoSDefendStatus": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（basic表示基础防护；bgp表示独享包；bgp-multip表示共享包；bgpip表示高防IP；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源实例ID，只有当Business不是基础防护时才需要填写此字段；"
      },
      {
        "name": "Ip",
        "desc": "基础防护的IP，只有当Business为基础防护时才需要填写此字段；"
      },
      {
        "name": "BizType",
        "desc": "只有当Business为基础防护时才需要填写此字段，IP所属的产品类型，取值[public（CVM产品），bm（黑石产品），eni（弹性网卡），vpngw（VPN网关）， natgw（NAT网关），waf（Web应用安全产品），fpc（金融产品），gaap（GAAP产品）, other(托管IP)]"
      },
      {
        "name": "DeviceType",
        "desc": "只有当Business为基础防护时才需要填写此字段，IP所属的产品子类，取值[cvm（CVM），lb（负载均衡器），eni（弹性网卡），vpngw（VPN），natgw（NAT），waf（WAF），fpc（金融），gaap（GAAP），other（托管IP），eip（黑石弹性IP）]"
      },
      {
        "name": "InstanceId",
        "desc": "只有当Business为基础防护时才需要填写此字段，IP所属的资源实例ID，当绑定新IP时必须填写此字段；例如是弹性网卡的IP，则InstanceId填写弹性网卡的ID(eni-*);"
      },
      {
        "name": "IPRegion",
        "desc": "只有当Business为基础防护时才需要填写此字段，表示IP所属的地域，取值：\n\"bj\":     华北地区(北京)\n\"cd\":     西南地区(成都)\n\"cq\":     西南地区(重庆)\n\"gz\":     华南地区(广州)\n\"gzopen\": 华南地区(广州Open)\n\"hk\":     中国香港\n\"kr\":     东南亚地区(首尔)\n\"sh\":     华东地区(上海)\n\"shjr\":   华东地区(上海金融)\n\"szjr\":   华南地区(深圳金融)\n\"sg\":     东南亚地区(新加坡)\n\"th\":     东南亚地区(泰国)\n\"de\":     欧洲地区(德国)\n\"usw\":    美国西部（硅谷）\n\"ca\":     北美地区(多伦多)\n\"jp\":     日本\n\"hzec\":   杭州\n\"in\":     印度\n\"use\":    美东地区（弗吉尼亚）\n\"ru\":     俄罗斯\n\"tpe\":    中国台湾\n\"nj\":     南京"
      }
    ],
    "desc": "获取DDoS防护状态（临时关闭状态），支持产品：基础防护，独享包，共享包，高防IP，高防IP专业版；调用此接口是获取当前是否有设置临时关闭DDoS防护状态，如果有设置会返回临时关闭的时长等参数。"
  },
  "DescribeCCAlarmThreshold": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（shield表示棋牌；bgpip表示高防IP；bgp表示高防包；bgp-multip表示多ip高防包；net表示高防IP专业版）"
      },
      {
        "name": "RsId",
        "desc": "资源ID,字符串类型"
      }
    ],
    "desc": "获取高防包、高防IP、高防IP专业版、棋牌盾产品设置CC攻击的告警通知阈值"
  },
  "DescribePcap": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源实例ID"
      },
      {
        "name": "StartTime",
        "desc": "攻击事件的开始时间，格式为\"2018-08-28 07:00:00\""
      },
      {
        "name": "EndTime",
        "desc": "攻击事件的结束时间，格式为\"2018-08-28 07:02:00\""
      },
      {
        "name": "Ip",
        "desc": "资源的IP，只有当Business为net时才需要填写资源实例下的IP；"
      }
    ],
    "desc": "下载攻击事件的pcap包"
  },
  "DescribeNewL4Rules": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP）"
      },
      {
        "name": "Ip",
        "desc": "指定IP查询"
      },
      {
        "name": "VirtualPort",
        "desc": "指定高防IP端口查询"
      },
      {
        "name": "Limit",
        "desc": "一页条数，填0表示不分页"
      },
      {
        "name": "Offset",
        "desc": "页起始偏移，取值为(页码-1)*一页条数"
      }
    ],
    "desc": "获取L4转发规则"
  },
  "CreateNewL7Rules": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP）"
      },
      {
        "name": "IdList",
        "desc": "资源ID列表"
      },
      {
        "name": "VipList",
        "desc": "资源IP列表"
      },
      {
        "name": "Rules",
        "desc": "规则列表"
      }
    ],
    "desc": "添加7层转发规则"
  },
  "ModifyElasticLimit": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "Limit",
        "desc": "弹性防护阈值，取值[0 10000 20000 30000 40000 50000 60000 70000 80000 90000 100000 120000 150000 200000 250000 300000 400000 600000 800000 220000 310000 110000 270000 610000]"
      }
    ],
    "desc": "修改弹性防护阈值"
  },
  "DescribeDDoSNetIpLog": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "StartTime",
        "desc": "攻击开始时间"
      },
      {
        "name": "EndTime",
        "desc": "攻击结束时间"
      }
    ],
    "desc": "获取高防IP专业版资源的DDoSIP攻击日志"
  },
  "ModifyCCAlarmThreshold": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（shield表示棋牌；bgpip表示高防IP；bgp表示高防包；bgp-multip表示多ip高防包；net表示高防IP专业版）"
      },
      {
        "name": "RsId",
        "desc": "资源ID,字符串类型"
      },
      {
        "name": "AlarmThreshold",
        "desc": "告警阈值，大于0（目前排定的值），后台设置默认值为1000"
      },
      {
        "name": "IpList",
        "desc": "资源关联的IP列表，高防包未绑定时，传空数组，高防IP专业版传多个IP的数据"
      }
    ],
    "desc": "为高防包、高防IP、高防IP专业版、棋牌盾产品设置CC攻击的告警通知阈值"
  },
  "DescribeDDoSEvList": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版；basic表示DDoS基础防护）"
      },
      {
        "name": "StartTime",
        "desc": "开始时间"
      },
      {
        "name": "EndTime",
        "desc": "结束时间"
      },
      {
        "name": "Id",
        "desc": "资源实例ID，当Business为basic时，此字段不用填写（因为基础防护没有资源实例）"
      },
      {
        "name": "IpList",
        "desc": "资源的IP"
      },
      {
        "name": "OverLoad",
        "desc": "是否超过弹性防护峰值，取值[yes(是)，no(否)]，填写空字符串时表示不进行过滤"
      },
      {
        "name": "Limit",
        "desc": "一页条数，填0表示不分页"
      },
      {
        "name": "Offset",
        "desc": "页起始偏移，取值为(页码-1)*一页条数"
      }
    ],
    "desc": "获取DDoS攻击事件列表"
  },
  "DescribeIpBlockList": {
    "params": [],
    "desc": "获取IP封堵列表"
  },
  "DescribeL4HealthConfig": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "RuleIdList",
        "desc": "规则ID数组，当导出所有规则的健康检查配置则不填或填空数组；"
      }
    ],
    "desc": "导出四层健康检查配置"
  },
  "DescribeSecIndex": {
    "params": [],
    "desc": "获取本月安全统计"
  },
  "DescribeSchedulingDomainList": {
    "params": [
      {
        "name": "Limit",
        "desc": "一页条数，填0表示不分页"
      },
      {
        "name": "Offset",
        "desc": "页起始偏移，取值为(页码-1)*一页条数"
      },
      {
        "name": "Domain",
        "desc": "可选，筛选特定的域名"
      }
    ],
    "desc": "获取调度域名列表"
  },
  "DescribeCCFrequencyRules": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "RuleId",
        "desc": "7层转发规则ID（通过获取7层转发规则接口可以获取规则ID）；当填写时表示获取转发规则的访问频率控制规则；"
      }
    ],
    "desc": "获取CC防护的访问频率控制规则"
  },
  "DeleteDDoSPolicyCase": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）"
      },
      {
        "name": "SceneId",
        "desc": "策略场景ID"
      }
    ],
    "desc": "删除策略场景"
  },
  "DeleteL7Rules": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "RuleIdList",
        "desc": "规则ID列表"
      }
    ],
    "desc": "删除七层转发规则"
  },
  "CreateNewL4Rules": {
    "params": [
      {
        "name": "Business",
        "desc": "高防产品代号：bgpip"
      },
      {
        "name": "IdList",
        "desc": "添加规则资源列表"
      },
      {
        "name": "VipList",
        "desc": "添加规则IP列表"
      },
      {
        "name": "Rules",
        "desc": "规则列表"
      }
    ],
    "desc": "添加L4转发规则"
  },
  "CreateL4Rules": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "Rules",
        "desc": "规则列表"
      }
    ],
    "desc": "添加L4转发规则"
  },
  "DescribeBaradData": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源实例ID"
      },
      {
        "name": "MetricName",
        "desc": "指标名，取值：\nconnum表示TCP活跃连接数；\nnew_conn表示新建TCP连接数；\ninactive_conn表示非活跃连接数;\nintraffic表示入流量；\nouttraffic表示出流量；\nalltraffic表示出流量和入流量之和；\ninpkg表示入包速率；\noutpkg表示出包速率；"
      },
      {
        "name": "Period",
        "desc": "统计时间粒度，单位秒（300表示5分钟；3600表示小时；86400表示天）"
      },
      {
        "name": "StartTime",
        "desc": "统计开始时间，秒部分保持为0，分钟部分为5的倍数"
      },
      {
        "name": "EndTime",
        "desc": "统计结束时间，秒部分保持为0，分钟部分为5的倍数"
      },
      {
        "name": "Statistics",
        "desc": "统计方式，取值：\nmax表示最大值；\nmin表示最小值；\navg表示均值；"
      },
      {
        "name": "ProtocolPort",
        "desc": "协议端口数组"
      },
      {
        "name": "Ip",
        "desc": "资源实例下的IP，只有当Business=net(高防IP专业版)时才必须填写资源的一个IP（因为高防IP专业版资源实例有多个IP，才需要指定）；"
      }
    ],
    "desc": "为大禹子产品提供业务转发指标数据的接口"
  },
  "ModifyCCFrequencyRules": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）"
      },
      {
        "name": "CCFrequencyRuleId",
        "desc": "CC的访问频率控制规则ID"
      },
      {
        "name": "Mode",
        "desc": "匹配规则，取值[\"include\"(前缀匹配)，\"equal\"(完全匹配)]"
      },
      {
        "name": "Period",
        "desc": "统计周期，单位秒，取值[10, 30, 60]"
      },
      {
        "name": "ReqNumber",
        "desc": "访问次数，取值[1-10000]"
      },
      {
        "name": "Act",
        "desc": "执行动作，取值[\"alg\"（人机识别）, \"drop\"（拦截）]"
      },
      {
        "name": "ExeDuration",
        "desc": "执行时间，单位秒，取值[1-900]"
      },
      {
        "name": "Uri",
        "desc": "URI字符串，必须以/开头，例如/abc/a.php，长度不超过31；当URI=/时，匹配模式只能选择前缀匹配；"
      },
      {
        "name": "UserAgent",
        "desc": "User-Agent字符串，长度不超过80"
      },
      {
        "name": "Cookie",
        "desc": "Cookie字符串，长度不超过40"
      }
    ],
    "desc": "修改CC防护的访问频率控制规则"
  },
  "CreateDDoSPolicy": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）"
      },
      {
        "name": "DropOptions",
        "desc": "协议禁用，必须填写且数组长度必须为1"
      },
      {
        "name": "Name",
        "desc": "策略名称"
      },
      {
        "name": "PortLimits",
        "desc": "端口禁用，当没有禁用端口时填空数组"
      },
      {
        "name": "IpAllowDenys",
        "desc": "IP黑白名单，当没有IP黑白名单时填空数组"
      },
      {
        "name": "PacketFilters",
        "desc": "报文过滤，当没有报文过滤时填空数组"
      },
      {
        "name": "WaterPrint",
        "desc": "水印策略参数，当没有启用水印功能时填空数组，最多只能传一条水印策略（即数组大小不超过1）"
      }
    ],
    "desc": "添加DDoS高级策略"
  },
  "ModifyCCPolicySwitch": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "SetId",
        "desc": "策略ID"
      },
      {
        "name": "Switch",
        "desc": "开关状态"
      }
    ],
    "desc": "修改CC自定义策略开关"
  },
  "ModifyNetReturnSwitch": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源实例ID"
      },
      {
        "name": "Status",
        "desc": "Status 表示回切开关，0: 关闭， 1:打开"
      },
      {
        "name": "Hour",
        "desc": "回切时长，单位：小时，取值[0,1,2,3,4,5,6;]当status=1时必选填写Hour>0"
      }
    ],
    "desc": "在客户收攻击或者被封堵时，切回到源站，并设置回切的时长"
  },
  "DescribeNewL4RulesErrHealth": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP）"
      },
      {
        "name": "RuleIdList",
        "desc": "规则ID列表"
      }
    ],
    "desc": "获取L4转发规则健康检查异常结果"
  },
  "DescribeSourceIpSegment": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      }
    ],
    "desc": "获取回源IP段，支持的产品：高防IP，高防IP专业版；"
  },
  "ModifyCCUrlAllow": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "Method",
        "desc": "=add表示添加，=delete表示删除"
      },
      {
        "name": "Type",
        "desc": "黑/白名单类型；取值[white(白名单)]"
      },
      {
        "name": "UrlList",
        "desc": "URL数组，URL格式如下：\nhttp://域名/cgi\nhttps://域名/cgi"
      },
      {
        "name": "Protocol",
        "desc": "可选字段，代表CC防护类型，取值[http（HTTP协议的CC防护），https（HTTPS协议的CC防护）]；当不填时，默认为HTTP协议的CC防护；当填写https时还需要填写Domain和RuleId字段；"
      },
      {
        "name": "Domain",
        "desc": "可选字段，表示HTTPS协议的7层转发规则域名（通过获取7层转发规则接口可以获取域名），只有当Protocol字段为https时才必须填写此字段；"
      },
      {
        "name": "RuleId",
        "desc": "可选字段，表示HTTPS协议的7层转发规则ID（通过获取7层转发规则接口可以获取规则ID），当添加并且Protocol=https时必须填写；\n当Method为delete时，可以不用填写此字段；"
      }
    ],
    "desc": "添加或删除CC的URL白名单"
  },
  "DescribeBasicDeviceThreshold": {
    "params": [
      {
        "name": "BasicIp",
        "desc": "查询的IP地址，取值如：1.1.1.1"
      },
      {
        "name": "BasicRegion",
        "desc": "查询IP所属地域，取值如：gz、bj、sh、hk等地域缩写"
      },
      {
        "name": "BasicBizType",
        "desc": "专区类型，取值如：公有云专区：public，黑石专区：bm, NAT服务器专区：nat，互联网通道：channel。"
      },
      {
        "name": "BasicDeviceType",
        "desc": "设备类型，取值如：服务器：cvm，公有云负载均衡：clb，黑石负载均衡：lb，NAT服务器：nat，互联网通道：channel."
      },
      {
        "name": "BasicCheckFlag",
        "desc": "有效性检查，取值为1"
      },
      {
        "name": "BasicIpInstance",
        "desc": "可选，IPInstance Nat 网关（如果查询的设备类型是NAT服务器，需要传此参数，通过nat资源查询接口获取）"
      },
      {
        "name": "BasicIspCode",
        "desc": "可选，运营商线路（如果查询的设备类型是NAT服务器，需要传此参数为5）"
      }
    ],
    "desc": "获取基础防护黑洞阈值"
  },
  "CreateUnblockIp": {
    "params": [
      {
        "name": "Ip",
        "desc": "IP"
      },
      {
        "name": "ActionType",
        "desc": "解封类型（user：自助解封；auto：自动解封； update：升级解封；bind：绑定高防包解封）"
      }
    ],
    "desc": "IP解封操作"
  },
  "ModifyNewL4Rule": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "Rule",
        "desc": "转发规则"
      }
    ],
    "desc": "修改4层转发规则"
  },
  "DeleteDDoSPolicy": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）"
      },
      {
        "name": "PolicyId",
        "desc": "策略ID"
      }
    ],
    "desc": "删除DDoS高级策略"
  },
  "DescribeDDoSNetCount": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "StartTime",
        "desc": "统计开始时间"
      },
      {
        "name": "EndTime",
        "desc": "统计结束时间"
      },
      {
        "name": "MetricName",
        "desc": "指标，取值[traffic（攻击协议流量, 单位KB）, pkg（攻击协议报文数）, classnum（攻击事件次数）]"
      }
    ],
    "desc": "获取高防IP专业版资源的DDoS攻击占比分析"
  },
  "DeleteCCSelfDefinePolicy": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "SetId",
        "desc": "策略ID"
      }
    ],
    "desc": "删除CC自定义策略"
  },
  "DescribePolicyCase": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）"
      },
      {
        "name": "SceneId",
        "desc": "策略场景ID"
      }
    ],
    "desc": "获取策略场景"
  },
  "DescribeActionLog": {
    "params": [
      {
        "name": "StartTime",
        "desc": "开始时间"
      },
      {
        "name": "EndTime",
        "desc": "结束时间"
      },
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）"
      },
      {
        "name": "Filter",
        "desc": "搜索值，只支持资源ID或用户UIN"
      },
      {
        "name": "Limit",
        "desc": "一页条数，填0表示不分页"
      },
      {
        "name": "Offset",
        "desc": "页起始偏移，取值为(页码-1)*一页条数"
      }
    ],
    "desc": "获取操作日志"
  },
  "ModifyL4Rules": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "Rule",
        "desc": "规则"
      }
    ],
    "desc": "修改L4转发规则"
  },
  "DescribeDDoSIpLog": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "Ip",
        "desc": "资源的IP"
      },
      {
        "name": "StartTime",
        "desc": "攻击开始时间"
      },
      {
        "name": "EndTime",
        "desc": "攻击结束时间"
      }
    ],
    "desc": "获取DDoSIP攻击日志"
  },
  "DescribeDDoSAlarmThreshold": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（shield表示棋牌；bgpip表示高防IP；bgp表示高防包；bgp-multip表示多ip高防包；net表示高防IP专业版）"
      },
      {
        "name": "RsId",
        "desc": "资源ID,字符串类型"
      }
    ],
    "desc": "获取高防包、高防IP、高防IP专业版、棋牌盾产品设置DDoS攻击的告警通知阈值"
  },
  "DescribePackIndex": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；bgp表示高防包；net表示高防IP专业版）"
      }
    ],
    "desc": "获取产品总览统计，支持高防包、高防IP、高防IP专业版；"
  },
  "DescribleNewL7Rules": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP）"
      },
      {
        "name": "Limit",
        "desc": "一页条数，填0表示不分页"
      },
      {
        "name": "Offset",
        "desc": "页起始偏移，取值为(页码-1)*一页条数"
      },
      {
        "name": "Domain",
        "desc": "域名搜索，选填，当需要搜索域名请填写"
      },
      {
        "name": "ProtocolList",
        "desc": "转发协议搜索，选填，取值[http, https, http/https]"
      },
      {
        "name": "StatusList",
        "desc": "状态搜索，选填，取值[0(规则配置成功)，1(规则配置生效中)，2(规则配置失败)，3(规则删除生效中)，5(规则删除失败)，6(规则等待配置)，7(规则等待删除)，8(规则待配置证书)]"
      },
      {
        "name": "Ip",
        "desc": "IP搜索，选填，当需要搜索IP请填写"
      }
    ],
    "desc": "获取7层规则"
  },
  "CreateBasicDDoSAlarmThreshold": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（basic表示DDoS基础防护）"
      },
      {
        "name": "Method",
        "desc": "=get表示读取告警阈值；=set表示设置告警阈值；"
      },
      {
        "name": "AlarmType",
        "desc": "可选，告警阈值类型，1-入流量，2-清洗流量；当Method为set时必须填写；"
      },
      {
        "name": "AlarmThreshold",
        "desc": "可选，告警阈值，当Method为set时必须填写；当设置阈值为0时表示清除告警阈值配置；"
      }
    ],
    "desc": "设置基础防护的DDoS告警阈值，只支持基础防护产品"
  },
  "ModifyDDoSThreshold": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "Threshold",
        "desc": "DDoS清洗阈值，取值[0, 60, 80, 100, 150, 200, 250, 300, 400, 500, 700, 1000];\n当设置值为0时，表示采用默认值；"
      }
    ],
    "desc": "修改DDoS清洗阈值"
  },
  "CreateL7RuleCert": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源实例ID，例如高防IP实例的ID，高防IP专业版实例的ID"
      },
      {
        "name": "RuleId",
        "desc": "规则ID"
      },
      {
        "name": "CertType",
        "desc": "证书类型，当为协议为HTTPS协议时必须填，取值[2(腾讯云托管证书)]"
      },
      {
        "name": "SSLId",
        "desc": "当证书来源为腾讯云托管证书时，此字段必须填写托管证书ID"
      },
      {
        "name": "Cert",
        "desc": "当证书来源为自有证书时，此字段必须填写证书内容；(因已不再支持自有证书，此字段已弃用，请不用填写此字段)"
      },
      {
        "name": "PrivateKey",
        "desc": "当证书来源为自有证书时，此字段必须填写证书密钥；(因已不再支持自有证书，此字段已弃用，请不用填写此字段)"
      }
    ],
    "desc": "配置7层转发规则的证书"
  },
  "ModifyDDoSAIStatus": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "Method",
        "desc": "=get表示读取AI防护状态；=set表示修改AI防护状态；"
      },
      {
        "name": "DDoSAI",
        "desc": "AI防护状态，取值[on，off]；当Method=set时必填；"
      }
    ],
    "desc": "读取或修改DDoS的AI防护状态"
  },
  "DescribeCCIpAllowDeny": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "Type",
        "desc": "黑或白名单，取值[white(白名单)，black(黑名单)]\n注意：此数组只能有一个值，不能同时获取黑名单和白名单"
      },
      {
        "name": "Limit",
        "desc": "分页参数"
      },
      {
        "name": "Offset",
        "desc": "分页参数"
      },
      {
        "name": "Protocol",
        "desc": "可选，代表HTTP协议或HTTPS协议的CC防护，取值[http（HTTP协议的CC防护），https（HTTPS协议的CC防护）]；"
      }
    ],
    "desc": "获取CC的IP黑白名单"
  },
  "CreateL4HealthConfig": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "HealthConfig",
        "desc": "四层健康检查配置数组"
      }
    ],
    "desc": "上传四层健康检查配置"
  },
  "DescribeResourceList": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgp表示独享包；bgp-multip表示共享包；bgpip表示高防IP；net表示高防IP专业版）"
      },
      {
        "name": "RegionList",
        "desc": "地域码搜索，可选，当不指定地域时空数组，当指定地域时，填地域码。例如：[\"gz\", \"sh\"]"
      },
      {
        "name": "Line",
        "desc": "线路搜索，可选，只有当获取高防IP资源列表是可以选填，取值为[1（BGP线路），2（南京电信），3（南京联通），99（第三方合作线路）]，当获取其他产品时请填空数组；"
      },
      {
        "name": "IdList",
        "desc": "资源ID搜索，可选，当不为空数组时表示获取指定资源的资源列表；"
      },
      {
        "name": "Name",
        "desc": "资源名称搜索，可选，当不为空字符串时表示按名称搜索资源；"
      },
      {
        "name": "IpList",
        "desc": "IP搜索列表，可选，当不为空时表示安装IP搜索资源；"
      },
      {
        "name": "Status",
        "desc": "资源状态搜索列表，可选，取值为[0（运行中）, 1（清洗中）, 2（封堵中）]，当填空数组时不进行状态搜索；"
      },
      {
        "name": "Expire",
        "desc": "即将到期搜索；可选，取值为[0（不搜索），1（搜索即将到期的资源）]"
      },
      {
        "name": "OderBy",
        "desc": "排序字段，可选"
      },
      {
        "name": "Limit",
        "desc": "一页条数，填0表示不分页"
      },
      {
        "name": "Offset",
        "desc": "页起始偏移，取值为(页码-1)*一页条数"
      },
      {
        "name": "CName",
        "desc": "高防IP专业版资源的CNAME，可选，只对高防IP专业版资源列表有效；"
      },
      {
        "name": "Domain",
        "desc": "高防IP专业版资源的域名，可选，只对高防IP专业版资源列表有效；"
      }
    ],
    "desc": "获取资源列表"
  },
  "CreateBoundIP": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgp表示独享包；bgp-multip表示共享包）"
      },
      {
        "name": "Id",
        "desc": "资源实例ID"
      },
      {
        "name": "BoundDevList",
        "desc": "绑定到资源实例的IP数组，当资源实例为高防包(独享包)时，数组只允许填1个IP；当没有要绑定的IP时可以为空数组；但是BoundDevList和UnBoundDevList至少有一个不为空；"
      },
      {
        "name": "UnBoundDevList",
        "desc": "与资源实例解绑的IP数组，当资源实例为高防包(独享包)时，数组只允许填1个IP；当没有要解绑的IP时可以为空数组；但是BoundDevList和UnBoundDevList至少有一个不为空；"
      },
      {
        "name": "CopyPolicy",
        "desc": "已弃用，不填"
      }
    ],
    "desc": "绑定IP到高防包实例，支持独享包、共享包；需要注意的是此接口绑定或解绑IP是异步接口，当处于绑定或解绑中时，则不允许再进行绑定或解绑，需要等待当前绑定或解绑完成。"
  },
  "ModifyDDoSPolicy": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）"
      },
      {
        "name": "PolicyId",
        "desc": "策略ID"
      },
      {
        "name": "DropOptions",
        "desc": "协议禁用，必须填写且数组长度必须为1"
      },
      {
        "name": "PortLimits",
        "desc": "端口禁用，当没有禁用端口时填空数组"
      },
      {
        "name": "IpAllowDenys",
        "desc": "IP黑白名单，当没有IP黑白名单时填空数组"
      },
      {
        "name": "PacketFilters",
        "desc": "报文过滤，当没有报文过滤时填空数组"
      },
      {
        "name": "WaterPrint",
        "desc": "水印策略参数，当没有启用水印功能时填空数组，最多只能传一条水印策略（即数组大小不超过1）"
      }
    ],
    "desc": "修改DDoS高级策略"
  },
  "ModifyDDoSPolicyCase": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）"
      },
      {
        "name": "SceneId",
        "desc": "策略场景ID"
      },
      {
        "name": "PlatformTypes",
        "desc": "开发平台，取值[PC（PC客户端）， MOBILE（移动端）， TV（电视端）， SERVER（主机）]"
      },
      {
        "name": "AppType",
        "desc": "细分品类，取值[WEB（网站）， GAME（游戏）， APP（应用）， OTHER（其他）]"
      },
      {
        "name": "AppProtocols",
        "desc": "应用协议，取值[tcp（TCP协议），udp（UDP协议），icmp（ICMP协议），all（其他协议）]"
      },
      {
        "name": "TcpSportStart",
        "desc": "TCP业务起始端口，取值(0, 65535]"
      },
      {
        "name": "TcpSportEnd",
        "desc": "TCP业务结束端口，取值(0, 65535]，必须大于等于TCP业务起始端口"
      },
      {
        "name": "UdpSportStart",
        "desc": "UDP业务起始端口，取值范围(0, 65535]"
      },
      {
        "name": "UdpSportEnd",
        "desc": "UDP业务结束端口，取值范围(0, 65535)，必须大于等于UDP业务起始端口"
      },
      {
        "name": "HasAbroad",
        "desc": "是否有海外客户，取值[no（没有）, yes（有）]"
      },
      {
        "name": "HasInitiateTcp",
        "desc": "是否会主动对外发起TCP请求，取值[no（不会）, yes（会）]"
      },
      {
        "name": "HasInitiateUdp",
        "desc": "是否会主动对外发起UDP业务请求，取值[no（不会）, yes（会）]"
      },
      {
        "name": "PeerTcpPort",
        "desc": "主动发起TCP请求的端口，取值范围(0, 65535]"
      },
      {
        "name": "PeerUdpPort",
        "desc": "主动发起UDP请求的端口，取值范围(0, 65535]"
      },
      {
        "name": "TcpFootprint",
        "desc": "TCP载荷的固定特征码，字符串长度小于512"
      },
      {
        "name": "UdpFootprint",
        "desc": "UDP载荷的固定特征码，字符串长度小于512"
      },
      {
        "name": "WebApiUrl",
        "desc": "Web业务的API的URL"
      },
      {
        "name": "MinTcpPackageLen",
        "desc": "TCP业务报文长度最小值，取值范围(0, 1500)"
      },
      {
        "name": "MaxTcpPackageLen",
        "desc": "TCP业务报文长度最大值，取值范围(0, 1500)，必须大于等于TCP业务报文长度最小值"
      },
      {
        "name": "MinUdpPackageLen",
        "desc": "UDP业务报文长度最小值，取值范围(0, 1500)"
      },
      {
        "name": "MaxUdpPackageLen",
        "desc": "UDP业务报文长度最大值，取值范围(0, 1500)，必须大于等于UDP业务报文长度最小值"
      },
      {
        "name": "HasVPN",
        "desc": "是否有VPN业务，取值[no（没有）, yes（有）]"
      },
      {
        "name": "TcpPortList",
        "desc": "TCP业务端口列表，同时支持单个端口和端口段，字符串格式，例如：80,443,700-800,53,1000-3000"
      },
      {
        "name": "UdpPortList",
        "desc": "UDP业务端口列表，同时支持单个端口和端口段，字符串格式，例如：80,443,700-800,53,1000-3000"
      }
    ],
    "desc": "修改策略场景"
  },
  "ModifyDDoSAlarmThreshold": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（shield表示棋牌；bgpip表示高防IP；bgp表示高防包；bgp-multip表示多ip高防包；net表示高防IP专业版）"
      },
      {
        "name": "RsId",
        "desc": "资源ID,字符串类型"
      },
      {
        "name": "AlarmType",
        "desc": "告警阈值类型，0-未设置，1-入流量，2-清洗流量"
      },
      {
        "name": "AlarmThreshold",
        "desc": "告警阈值，大于0（目前暂定的值）"
      },
      {
        "name": "IpList",
        "desc": "资源关联的IP列表，高防包未绑定时，传空数组，高防IP专业版传多个IP的数据"
      }
    ],
    "desc": "为高防包、高防IP、高防IP专业版、棋牌盾等产品设置DDoS攻击的告警通知阈值"
  },
  "DescribeDDoSNetEvInfo": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "StartTime",
        "desc": "攻击开始时间"
      },
      {
        "name": "EndTime",
        "desc": "攻击结束时间"
      }
    ],
    "desc": "获取高防IP专业版资源的DDoS攻击事件详情"
  },
  "DeleteCCFrequencyRules": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）"
      },
      {
        "name": "CCFrequencyRuleId",
        "desc": "CC防护的访问频率控制规则ID"
      }
    ],
    "desc": "删除CC防护的访问频率控制规则"
  },
  "ModifyL4KeepTime": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "RuleId",
        "desc": "规则ID"
      },
      {
        "name": "KeepEnable",
        "desc": "会话保持开关，取值[0(会话保持关闭)，1(会话保持开启)]"
      },
      {
        "name": "KeepTime",
        "desc": "会话保持时间，单位秒"
      }
    ],
    "desc": "修改L4转发规则的会话保持，支持的子产品：高防IP、高防IP专业版"
  },
  "DescribeL4RulesErrHealth": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      }
    ],
    "desc": "获取L4转发规则健康检查异常结果"
  },
  "CreateL7RulesUpload": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "Rules",
        "desc": "规则列表"
      }
    ],
    "desc": "批量上传7层转发规则"
  },
  "DescribeDDoSAttackIPRegionMap": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（shield表示棋牌；bgpip表示高防IP；bgp表示高防包；bgp-multip表示多ip高防包；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "StartTime",
        "desc": "统计开始时间"
      },
      {
        "name": "EndTime",
        "desc": "统计结束时间，最大可统计的时间范围是半年；"
      },
      {
        "name": "IpList",
        "desc": "指定资源的特定IP的攻击源，可选"
      }
    ],
    "desc": "获取DDoS攻击源IP地域分布图，支持全球攻击分布和国内省份攻击分布；"
  },
  "DescribeTransmitStatis": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版；bgp表示独享包；bgp-multip表示共享包）"
      },
      {
        "name": "Id",
        "desc": "资源实例ID"
      },
      {
        "name": "MetricName",
        "desc": "指标名，取值：\ntraffic表示流量带宽；\npkg表示包速率；"
      },
      {
        "name": "Period",
        "desc": "统计时间粒度（300表示5分钟；3600表示小时；86400表示天）"
      },
      {
        "name": "StartTime",
        "desc": "统计开始时间，秒部分保持为0，分钟部分为5的倍数"
      },
      {
        "name": "EndTime",
        "desc": "统计结束时间，秒部分保持为0，分钟部分为5的倍数"
      },
      {
        "name": "IpList",
        "desc": "资源的IP（当Business为bgp-multip时必填，且仅支持一个IP）；当不填写时，默认统计资源实例的所有IP；资源实例有多个IP（比如高防IP专业版）时，统计方式是求和；"
      }
    ],
    "desc": "获取业务转发统计数据，支持转发流量和转发包速率"
  },
  "ModifyCCLevel": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "Level",
        "desc": "CC防护等级，取值[default(正常), loose(宽松), strict(严格)];"
      },
      {
        "name": "Protocol",
        "desc": "可选字段，代表CC防护类型，取值[http（HTTP协议的CC防护），https（HTTPS协议的CC防护）]；当不填时，默认为HTTP协议的CC防护；当填写https时还需要填写RuleId字段；"
      },
      {
        "name": "RuleId",
        "desc": "表示7层转发规则ID（通过获取7层转发规则接口可以获取规则ID）；"
      }
    ],
    "desc": "修改CC防护等级"
  },
  "ModifyDDoSDefendStatus": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgp表示独享包；bgp-multip表示共享包；bgpip表示高防IP；net表示高防IP专业版；basic表示基础防护）"
      },
      {
        "name": "Status",
        "desc": "防护状态值，取值[0（关闭），1（开启）]"
      },
      {
        "name": "Hour",
        "desc": "关闭时长，单位小时，取值[0，1，2，3，4，5，6]；当Status=0表示关闭时，Hour必须大于0；"
      },
      {
        "name": "Id",
        "desc": "资源ID；当Business不是基础防护时必须填写此字段；"
      },
      {
        "name": "Ip",
        "desc": "基础防护的IP，只有当Business为基础防护时才需要填写此字段；"
      },
      {
        "name": "BizType",
        "desc": "只有当Business为基础防护时才需要填写此字段，IP所属的产品类型，取值[public（CVM产品），bm（黑石产品），eni（弹性网卡），vpngw（VPN网关）， natgw（NAT网关），waf（Web应用安全产品），fpc（金融产品），gaap（GAAP产品）, other(托管IP)]"
      },
      {
        "name": "DeviceType",
        "desc": "只有当Business为基础防护时才需要填写此字段，IP所属的产品子类，取值[cvm（CVM），lb（负载均衡器），eni（弹性网卡），vpngw（VPN），natgw（NAT），waf（WAF），fpc（金融），gaap（GAAP），other（托管IP），eip（黑石弹性IP）]"
      },
      {
        "name": "InstanceId",
        "desc": "只有当Business为基础防护时才需要填写此字段，IP所属的资源实例ID，当绑定新IP时必须填写此字段；例如是弹性网卡的IP，则InstanceId填写弹性网卡的ID(eni-*);"
      },
      {
        "name": "IPRegion",
        "desc": "只有当Business为基础防护时才需要填写此字段，表示IP所属的地域，取值：\n\"bj\":     华北地区(北京)\n\"cd\":     西南地区(成都)\n\"cq\":     西南地区(重庆)\n\"gz\":     华南地区(广州)\n\"gzopen\": 华南地区(广州Open)\n\"hk\":     中国香港\n\"kr\":     东南亚地区(首尔)\n\"sh\":     华东地区(上海)\n\"shjr\":   华东地区(上海金融)\n\"szjr\":   华南地区(深圳金融)\n\"sg\":     东南亚地区(新加坡)\n\"th\":     东南亚地区(泰国)\n\"de\":     欧洲地区(德国)\n\"usw\":    美国西部（硅谷）\n\"ca\":     北美地区(多伦多)\n\"jp\":     日本\n\"hzec\":   杭州\n\"in\":     印度\n\"use\":    美东地区（弗吉尼亚）\n\"ru\":     俄罗斯\n\"tpe\":    中国台湾\n\"nj\":     南京"
      }
    ],
    "desc": "开启或关闭DDoS防护状态，调用此接口允许临时关闭DDoS防护一段时间，等时间到了会自动开启DDoS防护；"
  },
  "DescribeUnBlockStatis": {
    "params": [],
    "desc": "获取黑洞解封次数"
  },
  "DescribeDDoSTrend": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版；basic表示DDoS基础防护）"
      },
      {
        "name": "Ip",
        "desc": "资源实例的IP"
      },
      {
        "name": "MetricName",
        "desc": "指标，取值[bps(攻击流量带宽，pps(攻击包速率))]"
      },
      {
        "name": "Period",
        "desc": "统计粒度，取值[300(5分钟)，3600(小时)，86400(天)]"
      },
      {
        "name": "StartTime",
        "desc": "统计开始时间"
      },
      {
        "name": "EndTime",
        "desc": "统计结束时间"
      },
      {
        "name": "Id",
        "desc": "资源实例ID，当Business为basic时，此字段不用填写（因为基础防护没有资源实例）"
      }
    ],
    "desc": "获取DDoS攻击流量带宽和攻击包速率数据"
  },
  "CreateNetReturn": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源实例ID"
      }
    ],
    "desc": "高防IP专业版一键切回源站"
  },
  "ModifyDDoSSwitch": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（basic表示基础防护）"
      },
      {
        "name": "Method",
        "desc": "=get表示读取DDoS防护状态；=set表示修改DDoS防护状态；"
      },
      {
        "name": "Ip",
        "desc": "基础防护的IP，只有当Business为基础防护时才需要填写此字段；"
      },
      {
        "name": "BizType",
        "desc": "只有当Business为基础防护时才需要填写此字段，IP所属的产品类型，取值[public（CVM产品），bm（黑石产品），eni（弹性网卡），vpngw（VPN网关）， natgw（NAT网关），waf（Web应用安全产品），fpc（金融产品），gaap（GAAP产品）, other(托管IP)]"
      },
      {
        "name": "DeviceType",
        "desc": "只有当Business为基础防护时才需要填写此字段，IP所属的产品子类，取值[cvm（CVM），lb（负载均衡器），eni（弹性网卡），vpngw（VPN），natgw（NAT），waf（WAF），fpc（金融），gaap（GAAP），other（托管IP），eip（黑石弹性IP）]"
      },
      {
        "name": "InstanceId",
        "desc": "只有当Business为基础防护时才需要填写此字段，IP所属的资源实例ID，当绑定新IP时必须填写此字段；例如是弹性网卡的IP，则InstanceId填写弹性网卡的ID(eni-*);"
      },
      {
        "name": "IPRegion",
        "desc": "只有当Business为基础防护时才需要填写此字段，表示IP所属的地域，取值：\n\"bj\":     华北地区(北京)\n\"cd\":     西南地区(成都)\n\"cq\":     西南地区(重庆)\n\"gz\":     华南地区(广州)\n\"gzopen\": 华南地区(广州Open)\n\"hk\":     中国香港\n\"kr\":     东南亚地区(首尔)\n\"sh\":     华东地区(上海)\n\"shjr\":   华东地区(上海金融)\n\"szjr\":   华南地区(深圳金融)\n\"sg\":     东南亚地区(新加坡)\n\"th\":     东南亚地区(泰国)\n\"de\":     欧洲地区(德国)\n\"usw\":    美国西部（硅谷）\n\"ca\":     北美地区(多伦多)\n\"jp\":     日本\n\"hzec\":   杭州\n\"in\":     印度\n\"use\":    美东地区（弗吉尼亚）\n\"ru\":     俄罗斯\n\"tpe\":    中国台湾\n\"nj\":     南京"
      },
      {
        "name": "Status",
        "desc": "可选字段，防护状态值，取值[0（关闭），1（开启）]；当Method为get时可以不填写此字段；"
      }
    ],
    "desc": "开启或关闭DDoS防护，只支持基础防护产品；"
  },
  "ModifyDDoSLevel": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "Method",
        "desc": "=get表示读取防护等级；=set表示修改防护等级"
      },
      {
        "name": "DDoSLevel",
        "desc": "防护等级，取值[low,middle,high]；当Method=set时必填"
      }
    ],
    "desc": "读取或修改DDoS的防护等级"
  },
  "DescribeDDoSAttackSource": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "StartTime",
        "desc": "起始时间"
      },
      {
        "name": "EndTime",
        "desc": "结束时间"
      },
      {
        "name": "Limit",
        "desc": "一页条数，填0表示不分页"
      },
      {
        "name": "Offset",
        "desc": "页起始偏移，取值为(页码-1)*一页条数"
      },
      {
        "name": "IpList",
        "desc": "获取指定资源的特定ip的攻击源，可选"
      }
    ],
    "desc": "获取DDoS攻击源列表"
  },
  "DeleteNewL7Rules": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP)"
      },
      {
        "name": "Rule",
        "desc": "删除规则列表"
      }
    ],
    "desc": "删除L7转发规则"
  },
  "DescribeCCEvList": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版；basic表示DDoS基础防护）"
      },
      {
        "name": "StartTime",
        "desc": "开始时间"
      },
      {
        "name": "EndTime",
        "desc": "结束时间"
      },
      {
        "name": "Id",
        "desc": "资源实例ID"
      },
      {
        "name": "IpList",
        "desc": "资源实例的IP，当business不为basic时，如果IpList不为空则Id也必须不能为空；"
      },
      {
        "name": "Limit",
        "desc": "一页条数，填0表示不分页"
      },
      {
        "name": "Offset",
        "desc": "页起始偏移，取值为(页码-1)*一页条数"
      }
    ],
    "desc": "获取CC攻击事件列表"
  },
  "ModifyDDoSWaterKey": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）"
      },
      {
        "name": "PolicyId",
        "desc": "策略ID"
      },
      {
        "name": "Method",
        "desc": "密钥操作，取值：[add（添加），delete（删除），open（开启），close（关闭），get（获取密钥）]"
      },
      {
        "name": "KeyId",
        "desc": "密钥ID，当添加密钥操作时可以不填或填0，其他操作时必须填写；"
      }
    ],
    "desc": "支持水印密钥的添加，删除，开启，关闭"
  },
  "DescribeInsurePacks": {
    "params": [
      {
        "name": "IdList",
        "desc": "可选字段，保险包套餐ID，当要获取指定ID（例如insure-000000xe）的保险包套餐时请填写此字段；"
      }
    ],
    "desc": "获取保险包套餐列表"
  },
  "DeleteL4Rules": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "RuleIdList",
        "desc": "规则ID列表"
      }
    ],
    "desc": "删除四层转发规则"
  },
  "DescribeDDoSNetEvList": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "StartTime",
        "desc": "开始时间"
      },
      {
        "name": "EndTime",
        "desc": "结束时间"
      },
      {
        "name": "Limit",
        "desc": "一页条数，填0表示不分页"
      },
      {
        "name": "Offset",
        "desc": "页起始偏移，取值为(页码-1)*一页条数"
      }
    ],
    "desc": "获取高防IP专业版资源的DDoS攻击事件列表"
  },
  "ModifyCCHostProtection": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "RuleId",
        "desc": "规则ID"
      },
      {
        "name": "Method",
        "desc": "开启/关闭CC域名防护，取值[open(表示开启)，close(表示关闭)]"
      }
    ],
    "desc": "开启或关闭CC域名防护"
  },
  "DescribleRegionCount": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；）"
      },
      {
        "name": "LineList",
        "desc": "根据线路统计，取值为[1（BGP线路），2（南京电信），3（南京联通），99（第三方合作线路）]；只对高防IP产品有效，其他产品此字段忽略"
      }
    ],
    "desc": "获取地域的资源实例数"
  },
  "CreateL7Rules": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "Rules",
        "desc": "规则列表"
      }
    ],
    "desc": "添加7层(网站)转发规则"
  },
  "DescribeIpUnBlockList": {
    "params": [
      {
        "name": "BeginTime",
        "desc": "开始时间"
      },
      {
        "name": "EndTime",
        "desc": "结束时间"
      },
      {
        "name": "Ip",
        "desc": "IP（不为空时，进行IP过滤）"
      },
      {
        "name": "Paging",
        "desc": "分页参数（不为空时，进行分页查询），此字段后面会弃用，请用Limit和Offset字段代替；"
      },
      {
        "name": "Limit",
        "desc": "一页条数，填0表示不分页"
      },
      {
        "name": "Offset",
        "desc": "页起始偏移，取值为(页码-1)*一页条数"
      }
    ],
    "desc": "获取IP解封记录"
  },
  "DescribeIPProductInfo": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgp表示独享包；bgp-multip表示共享包）"
      },
      {
        "name": "IpList",
        "desc": "IP列表"
      }
    ],
    "desc": "获取独享包或共享包IP对应的云资产信息，只支持独享包和共享包的IP"
  },
  "DescribeCCSelfDefinePolicy": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgp高防包；bgp-multip共享包）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "Limit",
        "desc": "拉取的条数"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      }
    ],
    "desc": "获取CC自定义策略"
  },
  "ModifyCCFrequencyRulesStatus": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "RuleId",
        "desc": "7层转发规则ID（通过获取7层转发规则接口可以获取规则ID）"
      },
      {
        "name": "Method",
        "desc": "开启或关闭，取值[\"on\"(开启)，\"off\"(关闭)]"
      }
    ],
    "desc": "开启或关闭CC防护的访问频率控制规则"
  },
  "ModifyCCThreshold": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版；basic表示基础防护）"
      },
      {
        "name": "Threshold",
        "desc": "CC防护阈值，取值(0 100 150 240 350 480 550 700 850 1000 1500 2000 3000 5000 10000 20000);\n当Business为高防IP、高防IP专业版时，其CC防护最大阈值跟资源的保底防护带宽有关，对应关系如下：\n  保底带宽: 最大C防护阈值\n  10:  20000,\n  20:  40000,\n  30:  70000,\n  40:  100000,\n  50:  150000,\n  60:  200000,\n  80:  250000,\n  100: 300000,"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "Protocol",
        "desc": "可选字段，代表CC防护类型，取值[http（HTTP协议的CC防护），https（HTTPS协议的CC防护）]；当不填时，默认为HTTP协议的CC防护；当填写https时还需要填写RuleId字段；"
      },
      {
        "name": "RuleId",
        "desc": "可选字段，表示HTTPS协议的7层转发规则ID（通过获取7层转发规则接口可以获取规则ID）；\n当Protocol=https时必须填写；"
      },
      {
        "name": "BasicIp",
        "desc": "查询的IP地址（仅基础防护提供），取值如：1.1.1.1"
      },
      {
        "name": "BasicRegion",
        "desc": "查询IP所属地域（仅基础防护提供），取值如：gz、bj、sh、hk等地域缩写"
      },
      {
        "name": "BasicBizType",
        "desc": "专区类型（仅基础防护提供），取值如：公有云专区：public，黑石专区：bm, NAT服务器专区：nat，互联网通道：channel。"
      },
      {
        "name": "BasicDeviceType",
        "desc": "设备类型（仅基础防护提供），取值如：服务器：cvm，公有云负载均衡：clb，黑石负载均衡：lb，NAT服务器：nat，互联网通道：channel."
      },
      {
        "name": "BasicIpInstance",
        "desc": "仅基础防护提供。可选，IPInstance Nat 网关（如果查询的设备类型是NAT服务器，需要传此参数，通过nat资源查询接口获取）"
      },
      {
        "name": "BasicIspCode",
        "desc": "仅基础防护提供。可选，运营商线路（如果查询的设备类型是NAT服务器，需要传此参数为5）"
      },
      {
        "name": "Domain",
        "desc": "可选字段，当协议取值HTTPS时，必填"
      }
    ],
    "desc": "修改CC的防护阈值"
  },
  "DescribleL4Rules": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "RuleIdList",
        "desc": "规则ID，可选参数，填写后获取指定的规则"
      },
      {
        "name": "Limit",
        "desc": "一页条数，填0表示不分页"
      },
      {
        "name": "Offset",
        "desc": "页起始偏移，取值为(页码-1)*一页条数"
      }
    ],
    "desc": "获取四层转发规则"
  },
  "ModifyNewDomainRules": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "Rule",
        "desc": "域名转发规则"
      }
    ],
    "desc": "修改7层转发规则"
  },
  "DescribeCCUrlAllow": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "Type",
        "desc": "黑或白名单，取值[white(白名单)]，目前只支持白名单\n注意：此数组只能有一个值，且只能为white"
      },
      {
        "name": "Limit",
        "desc": "分页参数"
      },
      {
        "name": "Offset",
        "desc": "分页参数"
      },
      {
        "name": "Protocol",
        "desc": "可选，代表HTTP协议或HTTPS协议的CC防护，取值[http（HTTP协议的CC防护），https（HTTPS协议的CC防护）]；"
      }
    ],
    "desc": "获取CC的Url白名单"
  },
  "DescribeL7HealthConfig": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "RuleIdList",
        "desc": "规则ID数组，当导出所有规则的健康检查配置则不填或填空数组；"
      }
    ],
    "desc": "导出七层健康检查配置"
  },
  "DescribeCCTrend": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版；basic表示DDoS基础防护）"
      },
      {
        "name": "Ip",
        "desc": "资源的IP"
      },
      {
        "name": "MetricName",
        "desc": "指标，取值[inqps(总请求峰值，dropqps(攻击请求峰值))]"
      },
      {
        "name": "Period",
        "desc": "统计粒度，取值[300(5分钟)，3600(小时)，86400(天)]"
      },
      {
        "name": "StartTime",
        "desc": "统计开始时间"
      },
      {
        "name": "EndTime",
        "desc": "统计结束时间"
      },
      {
        "name": "Id",
        "desc": "资源实例ID，当Business为basic时，此字段不用填写（因为基础防护没有资源实例）"
      }
    ],
    "desc": "获取CC攻击指标数据，包括总请求峰值(QPS)和攻击请求(QPS)"
  },
  "CreateCCFrequencyRules": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "RuleId",
        "desc": "7层转发规则ID（通过获取7层转发规则接口可以获取规则ID）"
      },
      {
        "name": "Mode",
        "desc": "匹配规则，取值[\"include\"(前缀匹配)，\"equal\"(完全匹配)]"
      },
      {
        "name": "Period",
        "desc": "统计周期，单位秒，取值[10, 30, 60]"
      },
      {
        "name": "ReqNumber",
        "desc": "访问次数，取值[1-10000]"
      },
      {
        "name": "Act",
        "desc": "执行动作，取值[\"alg\"（人机识别）, \"drop\"（拦截）]"
      },
      {
        "name": "ExeDuration",
        "desc": "执行时间，单位秒，取值[1-900]"
      },
      {
        "name": "Uri",
        "desc": "URI字符串，必须以/开头，例如/abc/a.php，长度不超过31；当URI=/时，匹配模式只能选择前缀匹配；"
      },
      {
        "name": "UserAgent",
        "desc": "User-Agent字符串，长度不超过80"
      },
      {
        "name": "Cookie",
        "desc": "Cookie字符串，长度不超过40"
      }
    ],
    "desc": "添加CC防护的访问频率控制规则"
  },
  "ModifyL7Rules": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "Rule",
        "desc": "规则"
      }
    ],
    "desc": "修改L7转发规则"
  },
  "DescribeBasicCCThreshold": {
    "params": [
      {
        "name": "BasicIp",
        "desc": "查询的IP地址，取值如：1.1.1.1"
      },
      {
        "name": "BasicRegion",
        "desc": "查询IP所属地域，取值如：gz、bj、sh、hk等地域缩写"
      },
      {
        "name": "BasicBizType",
        "desc": "专区类型，取值如：公有云专区：public，黑石专区：bm, NAT服务器专区：nat，互联网通道：channel。"
      },
      {
        "name": "BasicDeviceType",
        "desc": "设备类型，取值如：服务器：cvm，公有云负载均衡：clb，黑石负载均衡：lb，NAT服务器：nat，互联网通道：channel."
      },
      {
        "name": "BasicIpInstance",
        "desc": "可选，IPInstance Nat 网关（如果查询的设备类型是NAT服务器，需要传此参数，通过nat资源查询接口获取）"
      },
      {
        "name": "BasicIspCode",
        "desc": "可选，运营商线路（如果查询的设备类型是NAT服务器，需要传此参数为5）"
      }
    ],
    "desc": "获取基础防护CC防护阈值"
  },
  "CreateL7HealthConfig": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "HealthConfig",
        "desc": "七层健康检查配置数组"
      }
    ],
    "desc": "上传七层健康检查配置"
  },
  "DescribeResIpList": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）"
      },
      {
        "name": "IdList",
        "desc": "资源ID, 如果不填，则获取用户所有资源的IP"
      }
    ],
    "desc": "获取资源的IP列表"
  },
  "CreateInstanceName": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "Name",
        "desc": "资源实例名称，长度不超过32个字符"
      }
    ],
    "desc": "资源实例重命名，支持独享包、共享包、高防IP、高防IP专业版；"
  },
  "DescribeBGPIPL7RuleMaxCnt": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP）"
      },
      {
        "name": "Id",
        "desc": "资源实例ID"
      }
    ],
    "desc": "获取高防IP可添加的最多7层规则数量\n"
  },
  "ModifyResourceRenewFlag": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版；shield表示棋牌盾；bgp表示独享包；bgp-multip表示共享包；insurance表示保险包；staticpack表示三网套餐包）"
      },
      {
        "name": "Id",
        "desc": "资源Id"
      },
      {
        "name": "RenewFlag",
        "desc": "自动续费标记（0手动续费；1自动续费；2到期不续费）"
      }
    ],
    "desc": "修改资源自动续费标记"
  },
  "ModifyCCSelfDefinePolicy": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "SetId",
        "desc": "策略ID"
      },
      {
        "name": "Policy",
        "desc": "CC策略描述"
      }
    ],
    "desc": "修改CC自定义策略"
  },
  "DescribeDDoSEvInfo": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "资源ID"
      },
      {
        "name": "Ip",
        "desc": "资源的IP"
      },
      {
        "name": "StartTime",
        "desc": "攻击开始时间"
      },
      {
        "name": "EndTime",
        "desc": "攻击结束时间"
      }
    ],
    "desc": "获取DDoS攻击事件详情"
  },
  "DescribeDDoSPolicy": {
    "params": [
      {
        "name": "Business",
        "desc": "大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）"
      },
      {
        "name": "Id",
        "desc": "可选字段，资源ID，如果填写则表示该资源绑定的DDoS高级策略"
      }
    ],
    "desc": "获取DDoS高级策略"
  }
}