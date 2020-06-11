# -*- coding: utf-8 -*-
DESC = "gaap-2018-05-29"
INFO = {
  "DescribeProxyGroupList": {
    "params": [
      {
        "name": "Offset",
        "desc": "偏移量，默认值为0。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认值为20，最大值为100。"
      },
      {
        "name": "ProjectId",
        "desc": "项目ID。取值范围：\n-1，该用户下所有项目\n0，默认项目\n其他值，指定的项目"
      },
      {
        "name": "TagSet",
        "desc": "标签列表，当存在该字段时，拉取对应标签下的资源列表。\n最多支持5个标签，当存在两个或两个以上的标签时，满足其中任意一个标签时，该通道组会被拉取出来。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件。   \n每次请求的Filter.Values的上限为5。\nRealServerRegion - String - 是否必填：否 -（过滤条件）按照源站地域过滤，可参考DescribeDestRegions接口返回结果中的RegionId。"
      }
    ],
    "desc": "本接口（DescribeProxyGroupList）用于拉取通道组列表及各通道组基本信息。"
  },
  "OpenSecurityPolicy": {
    "params": [
      {
        "name": "ProxyId",
        "desc": "需开启安全策略的通道ID"
      },
      {
        "name": "PolicyId",
        "desc": "安全策略ID"
      }
    ],
    "desc": "开启安全策略"
  },
  "DescribeCertificates": {
    "params": [
      {
        "name": "CertificateType",
        "desc": "证书类型。其中：\n0，表示基础认证配置；\n1，表示客户端CA证书；\n2，表示服务器SSL证书；\n3，表示源站CA证书；\n4，表示通道SSL证书。\n-1，所有类型。\n默认为-1。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      },
      {
        "name": "Limit",
        "desc": "限制数量，默认为20。"
      }
    ],
    "desc": "本接口（DescribeCertificates）用来查询可以使用的证书列表。"
  },
  "CreateSecurityRules": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "安全策略ID"
      },
      {
        "name": "RuleList",
        "desc": "访问规则列表"
      }
    ],
    "desc": "添加安全策略规则"
  },
  "RemoveRealServers": {
    "params": [
      {
        "name": "RealServerIds",
        "desc": "源站Id列表"
      }
    ],
    "desc": "删除已添加的源站(服务器)IP或域名"
  },
  "DescribeHTTPSListeners": {
    "params": [
      {
        "name": "ProxyId",
        "desc": "过滤条件，通道ID"
      },
      {
        "name": "ListenerId",
        "desc": "过滤条件，根据监听器ID进行精确查询。"
      },
      {
        "name": "ListenerName",
        "desc": "过滤条件，根据监听器名称进行精确查询。"
      },
      {
        "name": "Port",
        "desc": "过滤条件，根据监听器端口进行精确查询。"
      },
      {
        "name": "Offset",
        "desc": "偏移量， 默认为0"
      },
      {
        "name": "Limit",
        "desc": "限制数量，默认为20"
      },
      {
        "name": "SearchValue",
        "desc": "过滤条件，支持按照端口或监听器名称进行模糊查询"
      },
      {
        "name": "GroupId",
        "desc": "过滤条件，通道组ID"
      }
    ],
    "desc": "本接口（DescribeHTTPSListeners）用来查询HTTPS监听器信息。"
  },
  "CreateHTTPSListener": {
    "params": [
      {
        "name": "ListenerName",
        "desc": "监听器名称"
      },
      {
        "name": "Port",
        "desc": "监听器端口，基于同种传输层协议（TCP 或 UDP）的监听器，端口不可重复"
      },
      {
        "name": "CertificateId",
        "desc": "服务器证书ID"
      },
      {
        "name": "ForwardProtocol",
        "desc": "加速通道转发到源站的协议类型：HTTP | HTTPS"
      },
      {
        "name": "ProxyId",
        "desc": "通道ID，与GroupId之间只能设置一个。表示创建通道的监听器。"
      },
      {
        "name": "AuthType",
        "desc": "认证类型，其中：\n0，单向认证；\n1，双向认证。\n默认使用单向认证。"
      },
      {
        "name": "ClientCertificateId",
        "desc": "客户端CA单证书ID，仅当双向认证时设置该参数或PolyClientCertificateIds参数"
      },
      {
        "name": "PolyClientCertificateIds",
        "desc": "新的客户端多CA证书ID，仅当双向认证时设置该参数或设置ClientCertificateId参数"
      },
      {
        "name": "GroupId",
        "desc": "通道组ID，与ProxyId之间只能设置一个。表示创建通道组的监听器。"
      }
    ],
    "desc": "该接口（CreateHTTPSListener）用于在通道实例下创建HTTPS协议类型的监听器。"
  },
  "DeleteSecurityPolicy": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "策略ID"
      }
    ],
    "desc": "删除安全策略"
  },
  "SetAuthentication": {
    "params": [
      {
        "name": "ListenerId",
        "desc": "监听器ID。"
      },
      {
        "name": "Domain",
        "desc": "需要进行高级配置的域名，该域名为监听器下的转发规则的域名。"
      },
      {
        "name": "BasicAuth",
        "desc": "基础认证开关，其中：\n0，关闭基础认证；\n1，开启基础认证。\n默认为0。"
      },
      {
        "name": "GaapAuth",
        "desc": "通道认证开关，用于源站对Gaap的认证，其中：\n0，关闭通道认证；\n1，开启通道认证。\n默认为0。"
      },
      {
        "name": "RealServerAuth",
        "desc": "源站认证开关，用于Gaap对服务器的认证，其中：\n0，关闭源站认证；\n1，开启源站认证。\n默认为0。"
      },
      {
        "name": "BasicAuthConfId",
        "desc": "基础认证配置ID，从证书管理页获取。"
      },
      {
        "name": "GaapCertificateId",
        "desc": "通道SSL证书ID，从证书管理页获取。"
      },
      {
        "name": "RealServerCertificateId",
        "desc": "源站CA证书ID，从证书管理页获取。源站认证时，填写该参数或RealServerCertificateId参数"
      },
      {
        "name": "RealServerCertificateDomain",
        "desc": "源站证书域名。"
      },
      {
        "name": "PolyRealServerCertificateIds",
        "desc": "多源站CA证书ID，从证书管理页获取。源站认证时，填写该参数或RealServerCertificateId参数"
      }
    ],
    "desc": "本接口（SetAuthentication）用于通道的高级认证配置，包括认证方式选择，以及各种认证方式对应的证书选择。仅支持Version3.0的通道。"
  },
  "DeleteRule": {
    "params": [
      {
        "name": "ListenerId",
        "desc": "7层监听器ID"
      },
      {
        "name": "RuleId",
        "desc": "转发规则ID"
      },
      {
        "name": "Force",
        "desc": "是否可以强制删除已绑定源站的转发规则，0非强制，1强制"
      }
    ],
    "desc": "该接口（DeleteRule）用于删除HTTP/HTTPS监听器的转发规则。"
  },
  "DeleteDomainErrorPageInfo": {
    "params": [
      {
        "name": "ErrorPageId",
        "desc": "定制错误响应页的唯一ID，请参考CreateDomainErrorPageInfo的响应"
      }
    ],
    "desc": "删除域名的定制错误"
  },
  "ModifyCertificate": {
    "params": [
      {
        "name": "ListenerId",
        "desc": "监听器实例ID"
      },
      {
        "name": "Domain",
        "desc": "需要修改证书的域名"
      },
      {
        "name": "CertificateId",
        "desc": "新的服务器证书ID。其中：\n当CertificateId=default时，表示使用监听器的证书。"
      },
      {
        "name": "ClientCertificateId",
        "desc": "新的客户端证书ID。其中：\n当ClientCertificateId=default时，表示使用监听器的证书。\n仅当采用双向认证方式时，需要设置该参数或者PolyClientCertificateIds。"
      },
      {
        "name": "PolyClientCertificateIds",
        "desc": "新的多客户端证书ID列表。其中：\n仅当采用双向认证方式时，需要设置该参数或ClientCertificateId参数。"
      }
    ],
    "desc": "本接口（ModifyCertificate）用于修改监听器下的域名对应的证书。该接口仅适用于version3.0的通道。"
  },
  "DescribeProxyStatistics": {
    "params": [
      {
        "name": "ProxyId",
        "desc": "通道ID"
      },
      {
        "name": "StartTime",
        "desc": "起始时间(2019-03-25 12:00:00)"
      },
      {
        "name": "EndTime",
        "desc": "结束时间(2019-03-25 12:00:00)"
      },
      {
        "name": "MetricNames",
        "desc": "统计指标名称列表，支持: 入带宽:InBandwidth, 出带宽:OutBandwidth, 并发:Concurrent, 入包量:InPackets, 出包量:OutPackets, 丢包率:PacketLoss, 延迟:Latency"
      },
      {
        "name": "Granularity",
        "desc": "监控粒度，目前支持60，300，3600，86400，单位：秒。\n当时间范围不超过3天，支持最小粒度60秒；\n当时间范围不超过7天，支持最小粒度300秒；\n当时间范围不超过30天，支持最小粒度3600秒。"
      }
    ],
    "desc": "该接口用于查询监听器统计数据，包括出入带宽，出入包量，并发，丢包和时延数据。支持300, 3600和86400的细粒度，取值为细粒度范围内最大值。"
  },
  "CreateRule": {
    "params": [
      {
        "name": "ListenerId",
        "desc": "7层监听器ID"
      },
      {
        "name": "Domain",
        "desc": "转发规则的域名"
      },
      {
        "name": "Path",
        "desc": "转发规则的路径"
      },
      {
        "name": "RealServerType",
        "desc": "转发规则对应源站的类型，支持IP和DOMAIN类型。"
      },
      {
        "name": "Scheduler",
        "desc": "规则转发源站调度策略，支持轮询（rr），加权轮询（wrr），最小连接数（lc）。"
      },
      {
        "name": "HealthCheck",
        "desc": "规则是否开启健康检查，1开启，0关闭。"
      },
      {
        "name": "CheckParams",
        "desc": "源站健康检查相关参数"
      },
      {
        "name": "ForwardProtocol",
        "desc": "加速通道转发到源站的协议类型：支持HTTP或HTTPS。\n不传递该字段时表示使用对应监听器的ForwardProtocol。"
      },
      {
        "name": "ForwardHost",
        "desc": "加速通道转发到远照的host，不设置该参数时，使用默认的host设置，即客户端发起的http请求的host。"
      }
    ],
    "desc": "该接口（CreateRule）用于创建HTTP/HTTPS监听器转发规则。"
  },
  "DescribeDestRegions": {
    "params": [],
    "desc": "本接口（DescribeDestRegions）用于查询源站区域，即源站服务器所在区域。"
  },
  "CreateDomainErrorPageInfo": {
    "params": [
      {
        "name": "ListenerId",
        "desc": "监听器ID"
      },
      {
        "name": "Domain",
        "desc": "域名"
      },
      {
        "name": "ErrorNos",
        "desc": "原始错误码"
      },
      {
        "name": "Body",
        "desc": "新的响应包体"
      },
      {
        "name": "NewErrorNo",
        "desc": "新错误码"
      },
      {
        "name": "ClearHeaders",
        "desc": "需要删除的响应头"
      },
      {
        "name": "SetHeaders",
        "desc": "需要设置的响应头"
      }
    ],
    "desc": "定制域名指定错误码的错误响应"
  },
  "DescribeProxyGroupStatistics": {
    "params": [
      {
        "name": "GroupId",
        "desc": "通道组ID"
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
        "name": "MetricNames",
        "desc": "统计指标名称列表，支持: 入带宽:InBandwidth, 出带宽:OutBandwidth, 并发:Concurrent, 入包量:InPackets, 出包量:OutPackets"
      },
      {
        "name": "Granularity",
        "desc": "监控粒度，目前支持60，300，3600，86400，单位：秒。\n当时间范围不超过1天，支持最小粒度60秒；\n当时间范围不超过7天，支持最小粒度3600秒；\n当时间范围不超过30天，支持最小粒度86400秒。"
      }
    ],
    "desc": "该接口用于查询监听器统计数据，包括出入带宽，出入包量，并发数据。支持300, 3600和86400的细粒度，取值为细粒度范围内最大值。"
  },
  "DescribeSecurityPolicyDetail": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "安全策略ID"
      }
    ],
    "desc": "获取安全策略详情"
  },
  "ModifyDomain": {
    "params": [
      {
        "name": "ListenerId",
        "desc": "7层监听器ID"
      },
      {
        "name": "OldDomain",
        "desc": "修改前的域名信息"
      },
      {
        "name": "NewDomain",
        "desc": "修改后的域名信息"
      },
      {
        "name": "CertificateId",
        "desc": "服务器SSL证书ID，仅适用于version3.0的通道。其中：\n不带该字段时，表示使用原证书；\n携带该字段时并且CertificateId=default，表示使用监听器证书；\n其他情况，使用该CertificateId指定的证书。"
      },
      {
        "name": "ClientCertificateId",
        "desc": "客户端CA证书ID，仅适用于version3.0的通道。其中：\n不带该字段和PolyClientCertificateIds时，表示使用原证书；\n携带该字段时并且ClientCertificateId=default，表示使用监听器证书；\n其他情况，使用该ClientCertificateId或PolyClientCertificateIds指定的证书。"
      },
      {
        "name": "PolyClientCertificateIds",
        "desc": "客户端CA证书ID，仅适用于version3.0的通道。其中：\n不带该字段和ClientCertificateId时，表示使用原证书；\n携带该字段时并且ClientCertificateId=default，表示使用监听器证书；\n其他情况，使用该ClientCertificateId或PolyClientCertificateIds指定的证书。"
      }
    ],
    "desc": "本接口（ModifyDomain）用于监听器下的域名。当通道版本为3.0时，支持对该域名所对应的证书修改。"
  },
  "ModifyCertificateAttributes": {
    "params": [
      {
        "name": "CertificateId",
        "desc": "证书ID。"
      },
      {
        "name": "CertificateAlias",
        "desc": "证书名字。长度不超过50个字符。"
      }
    ],
    "desc": "本接口（ModifyCertificateAttributes）用于修改证书，包括证明名字以及证书内容。"
  },
  "CloseProxies": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "（旧参数，请切换到ProxyIds）通道的实例ID。"
      },
      {
        "name": "ClientToken",
        "desc": "用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。\n更多详细信息请参阅：如何保证幂等性。"
      },
      {
        "name": "ProxyIds",
        "desc": "（新参数）通道的实例ID。"
      }
    ],
    "desc": "本接口（CloseProxies）用于关闭通道。通道关闭后，不再产生流量，但每天仍然收取通道基础配置费用。"
  },
  "OpenProxies": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "（旧参数，请切换到ProxyIds）通道的实例ID列表。"
      },
      {
        "name": "ClientToken",
        "desc": "用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。\n更多详细信息请参阅：如何保证幂等性。"
      },
      {
        "name": "ProxyIds",
        "desc": "（新参数）通道的实例ID列表。"
      }
    ],
    "desc": "该接口（OpenProxies）用于开启一条或者多条通道。"
  },
  "ModifyRealServerName": {
    "params": [
      {
        "name": "RealServerName",
        "desc": "源站名称"
      },
      {
        "name": "RealServerId",
        "desc": "源站ID"
      }
    ],
    "desc": "本接口（ModifyRealServerName）用于修改源站的名称"
  },
  "DescribeHTTPListeners": {
    "params": [
      {
        "name": "ProxyId",
        "desc": "通道ID"
      },
      {
        "name": "ListenerId",
        "desc": "过滤条件，按照监听器ID进行精确查询"
      },
      {
        "name": "ListenerName",
        "desc": "过滤条件，按照监听器名称进行精确查询"
      },
      {
        "name": "Port",
        "desc": "过滤条件，按照监听器端口进行精确查询"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0"
      },
      {
        "name": "Limit",
        "desc": "限制数量，默认为20个"
      },
      {
        "name": "SearchValue",
        "desc": "过滤条件，支持按照端口或监听器名称进行模糊查询，该参数不能与ListenerName和Port同时使用"
      },
      {
        "name": "GroupId",
        "desc": "通道组ID"
      }
    ],
    "desc": "该接口（DescribeHTTPListeners）用来查询HTTP监听器信息。"
  },
  "CheckProxyCreate": {
    "params": [
      {
        "name": "AccessRegion",
        "desc": "通道的接入(加速)区域。取值可通过接口DescribeAccessRegionsByDestRegion获取到"
      },
      {
        "name": "RealServerRegion",
        "desc": "通道的源站区域。取值可通过接口DescribeDestRegions获取到"
      },
      {
        "name": "Bandwidth",
        "desc": "通道带宽上限，单位：Mbps。"
      },
      {
        "name": "Concurrent",
        "desc": "通道并发量上限，表示同时在线的连接数，单位：万。"
      },
      {
        "name": "GroupId",
        "desc": "如果在通道组下创建通道，需要填写通道组的ID"
      }
    ],
    "desc": "本接口(CheckProxyCreate)用于查询能否创建指定配置的加速通道。"
  },
  "OpenProxyGroup": {
    "params": [
      {
        "name": "GroupId",
        "desc": "通道组实例 ID"
      }
    ],
    "desc": "该接口（OpenProxyGroup）用于开启一条通道组中的所有通道"
  },
  "DescribeAccessRegions": {
    "params": [],
    "desc": "本接口（DescribeAccessRegions）用于查询加速区域，即客户端接入区域。"
  },
  "DeleteSecurityRules": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "安全策略ID"
      },
      {
        "name": "RuleIdList",
        "desc": "访问规则ID列表"
      }
    ],
    "desc": "删除安全策略规则"
  },
  "DescribeProxyGroupDetails": {
    "params": [
      {
        "name": "GroupId",
        "desc": "通道组ID。"
      }
    ],
    "desc": "本接口（DescribeProxyGroupDetails）用于查询通道组详情。"
  },
  "CreateProxy": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "通道的项目ID。"
      },
      {
        "name": "ProxyName",
        "desc": "通道名称。"
      },
      {
        "name": "AccessRegion",
        "desc": "接入地域。"
      },
      {
        "name": "Bandwidth",
        "desc": "通道带宽上限，单位：Mbps。"
      },
      {
        "name": "Concurrent",
        "desc": "通道并发量上限，表示同时在线的连接数，单位：万。"
      },
      {
        "name": "RealServerRegion",
        "desc": "源站地域。当GroupId存在时，源站地域为通道组的源站地域,此时可不填该字段。当GroupId不存在时，需要填写该字段"
      },
      {
        "name": "ClientToken",
        "desc": "用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。\n更多详细信息请参阅：如何保证幂等性。"
      },
      {
        "name": "GroupId",
        "desc": "通道所在的通道组ID，当在通道组中创建通道时必带，否则忽略该字段。"
      },
      {
        "name": "TagSet",
        "desc": "通道需要添加的标签列表。"
      },
      {
        "name": "ClonedProxyId",
        "desc": "被复制的通道ID。只有处于运行中状态的通道可以被复制。\n当设置该参数时，表示复制该通道。"
      },
      {
        "name": "BillingType",
        "desc": "计费方式 (0:按带宽计费，1:按流量计费 默认按带宽计费）"
      }
    ],
    "desc": "本接口（CreateProxy）用于创建/复制一个指定配置的加速通道。当复制通道时，需要设置新通道的基本配置参数，并设置ClonedProxyId来指定被复制的通道。"
  },
  "DeleteCertificate": {
    "params": [
      {
        "name": "CertificateId",
        "desc": "需要删除的证书ID。"
      }
    ],
    "desc": "本接口（DeleteCertificate）用于删除证书。"
  },
  "CreateSecurityPolicy": {
    "params": [
      {
        "name": "DefaultAction",
        "desc": "默认策略：ACCEPT或DROP"
      },
      {
        "name": "ProxyId",
        "desc": "加速通道ID"
      },
      {
        "name": "GroupId",
        "desc": "通道组ID"
      }
    ],
    "desc": "创建安全策略"
  },
  "DescribeProxies": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "（旧参数，请切换到ProxyIds）按照一个或者多个实例ID查询。每次请求的实例的上限为100。参数不支持同时指定InstanceIds和Filters。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件。   \n每次请求的Filters的上限为10，Filter.Values的上限为5。参数不支持同时指定InstanceIds和Filters。 \nProjectId - String - 是否必填：否 -（过滤条件）按照项目ID过滤。    \nAccessRegion - String - 是否必填：否 - （过滤条件）按照接入地域过滤。    \nRealServerRegion - String - 是否必填：否 - （过滤条件）按照源站地域过滤。\nGroupId - String - 是否必填：否 - （过滤条件）按照通道组ID过滤。"
      },
      {
        "name": "ProxyIds",
        "desc": "（新参数，替代InstanceIds）按照一个或者多个实例ID查询。每次请求的实例的上限为100。参数不支持同时指定InstanceIds和Filters。"
      },
      {
        "name": "TagSet",
        "desc": "标签列表，当存在该字段时，拉取对应标签下的资源列表。\n最多支持5个标签，当存在两个或两个以上的标签时，满足其中任意一个标签时，通道会被拉取出来。"
      },
      {
        "name": "Independent",
        "desc": "当该字段为1时，仅拉取非通道组的通道，\n当该字段为0时，仅拉取通道组的通道，\n不存在该字段时，拉取所有通道，包括独立通道和通道组通道。"
      }
    ],
    "desc": "本接口（DescribeProxies）用于查询通道实例列表。"
  },
  "ModifyHTTPListenerAttribute": {
    "params": [
      {
        "name": "ListenerId",
        "desc": "需要修改的监听器ID"
      },
      {
        "name": "ListenerName",
        "desc": "新的监听器名称"
      },
      {
        "name": "ProxyId",
        "desc": "通道ID"
      }
    ],
    "desc": "该接口（ModifyHTTPListenerAttribute）用于修改通道的HTTP监听器配置信息，目前仅支持修改监听器的名称。\n注意：通道组通道暂时不支持HTTP/HTTPS监听器。"
  },
  "ModifyProxiesProject": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "需要修改到的项目ID。"
      },
      {
        "name": "InstanceIds",
        "desc": "（旧参数，请切换到ProxyIds）一个或多个待操作的通道ID。"
      },
      {
        "name": "ClientToken",
        "desc": "用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。\n更多详细信息请参阅：如何保证幂等性。"
      },
      {
        "name": "ProxyIds",
        "desc": "（新参数）一个或多个待操作的通道ID。"
      }
    ],
    "desc": "本接口（ModifyProxiesProject）用于修改通道所属项目。"
  },
  "DescribeGroupDomainConfig": {
    "params": [
      {
        "name": "GroupId",
        "desc": "通道组ID。"
      }
    ],
    "desc": "本接口（DescribeGroupDomainConfig）用于获取通道组域名解析配置详情。"
  },
  "BindRuleRealServers": {
    "params": [
      {
        "name": "RuleId",
        "desc": "转发规则ID"
      },
      {
        "name": "RealServerBindSet",
        "desc": "需要绑定的源站信息列表。\n如果已经存在绑定的源站，则会覆盖更新成这个源站列表。\n当不带该字段时，表示解绑该规则上的所有源站。\n如果该规则的源站调度策略是加权轮询，需要填写源站权重 RealServerWeight, 不填或者其他调度类型默认源站权重为1。"
      }
    ],
    "desc": "该接口用于7层监听器的转发规则绑定源站。注意：本接口会解绑之前绑定的源站，绑定本次调用所选择的源站。"
  },
  "DeleteProxyGroup": {
    "params": [
      {
        "name": "GroupId",
        "desc": "需要删除的通道组ID。"
      },
      {
        "name": "Force",
        "desc": "强制删除标识。其中：\n0，不强制删除，\n1，强制删除。\n默认为0，当通道组中存在通道或通道组中存在监听器/规则绑定了源站时，且Force为0时，该操作会返回失败。"
      }
    ],
    "desc": "本接口（DeleteProxyGroup）用于删除通道组。"
  },
  "DescribeAccessRegionsByDestRegion": {
    "params": [
      {
        "name": "DestRegion",
        "desc": "源站区域：接口DescribeDestRegions返回DestRegionSet中的RegionId字段值"
      }
    ],
    "desc": "本接口（DescribeAccessRegionsByDestRegion）根据源站区域查询可用的加速区域列表"
  },
  "ModifyHTTPSListenerAttribute": {
    "params": [
      {
        "name": "ListenerId",
        "desc": "监听器ID"
      },
      {
        "name": "ProxyId",
        "desc": "通道ID， 若为单通道监听器，此项必须填写"
      },
      {
        "name": "ListenerName",
        "desc": "修改后的监听器名称"
      },
      {
        "name": "ForwardProtocol",
        "desc": "监听器后端转发与源站之间的协议类型"
      },
      {
        "name": "CertificateId",
        "desc": "修改后的监听器服务器证书ID"
      },
      {
        "name": "ClientCertificateId",
        "desc": "修改后的监听器客户端证书ID，不支持多客户端证书，多客户端证书新采用PolyClientCertificateIds字段"
      },
      {
        "name": "PolyClientCertificateIds",
        "desc": "新字段,修改后的监听器客户端证书ID"
      }
    ],
    "desc": "该接口（ModifyHTTPSListenerAttribute）用于修改HTTPS监听器配置，当前不支持通道组和v1版本通道。"
  },
  "CreateDomain": {
    "params": [
      {
        "name": "ListenerId",
        "desc": "监听器ID。"
      },
      {
        "name": "Domain",
        "desc": "需要创建的域名，一个监听器下最大支持100个域名。"
      },
      {
        "name": "CertificateId",
        "desc": "服务器证书，用于客户端与GAAP的HTTPS的交互。"
      },
      {
        "name": "ClientCertificateId",
        "desc": "客户端CA证书，用于客户端与GAAP的HTTPS的交互。\n仅当采用双向认证的方式时，需要设置该字段或PolyClientCertificateIds字段。"
      },
      {
        "name": "PolyClientCertificateIds",
        "desc": "客户端CA证书，用于客户端与GAAP的HTTPS的交互。\n仅当采用双向认证的方式时，需要设置该字段或ClientCertificateId字段。"
      }
    ],
    "desc": "本接口（CreateDomain）用于创建HTTP/HTTPS监听器的访问域名，客户端请求通过访问该域名来请求后端业务。\n该接口仅支持version3.0的通道。"
  },
  "ModifyRuleAttribute": {
    "params": [
      {
        "name": "ListenerId",
        "desc": "监听器ID"
      },
      {
        "name": "RuleId",
        "desc": "转发规则ID"
      },
      {
        "name": "Scheduler",
        "desc": "调度策略，其中：\nrr，轮询；\nwrr，加权轮询；\nlc，最小连接数。"
      },
      {
        "name": "HealthCheck",
        "desc": "源站健康检查开关，其中：\n1，开启；\n0，关闭。"
      },
      {
        "name": "CheckParams",
        "desc": "健康检查配置参数"
      },
      {
        "name": "Path",
        "desc": "转发规则路径"
      },
      {
        "name": "ForwardProtocol",
        "desc": "加速通道转发到源站的协议类型，支持：default, HTTP和HTTPS。\n当ForwardProtocol=default时，表示使用对应监听器的ForwardProtocol。"
      },
      {
        "name": "ForwardHost",
        "desc": "加速通道转发到源站的请求中携带的host。\n当ForwardHost=default时，使用规则的域名，其他情况为该字段所设置的值。"
      }
    ],
    "desc": "本接口（ModifyRuleAttribute）用于修改转发规则的信息，包括健康检查的配置以及转发策略。"
  },
  "DescribeCertificateDetail": {
    "params": [
      {
        "name": "CertificateId",
        "desc": "证书ID。"
      }
    ],
    "desc": "本接口（DescribeCertificateDetail）用于查询证书详情，包括证书ID，证书名字，证书类型，证书内容以及密钥等信息。"
  },
  "CloseSecurityPolicy": {
    "params": [
      {
        "name": "ProxyId",
        "desc": "通道ID"
      },
      {
        "name": "PolicyId",
        "desc": "安全组策略ID"
      }
    ],
    "desc": "关闭安全策略"
  },
  "ModifyGroupDomainConfig": {
    "params": [
      {
        "name": "GroupId",
        "desc": "通道组ID。"
      },
      {
        "name": "DefaultDnsIp",
        "desc": "域名解析默认访问IP或域名。"
      },
      {
        "name": "AccessRegionList",
        "desc": "就近接入区域配置。"
      }
    ],
    "desc": "本接口（ModifyGroupDomainConfig）用于配置通道组就近接入域名。"
  },
  "DescribeTCPListeners": {
    "params": [
      {
        "name": "ProxyId",
        "desc": "过滤条件，根据通道ID进行拉取，ProxyId/GroupId/ListenerId必须设置一个，但ProxyId和GroupId不能同时设置。"
      },
      {
        "name": "ListenerId",
        "desc": "过滤条件，根据监听器ID精确查询。\n当设置了ProxyId时，会检查该监听器是否归属于该通道。\n当设置了GroupId时，会检查该监听器是否归属于该通道组。"
      },
      {
        "name": "ListenerName",
        "desc": "过滤条件，根据监听器名称精确查询"
      },
      {
        "name": "Port",
        "desc": "过滤条件，根据监听器端口精确查询"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0"
      },
      {
        "name": "Limit",
        "desc": "限制数量，默认为20"
      },
      {
        "name": "GroupId",
        "desc": "过滤条件，根据通道组ID进行拉取，ProxyId/GroupId/ListenerId必须设置一个，但ProxyId和GroupId不能同时设置。"
      },
      {
        "name": "SearchValue",
        "desc": "过滤条件，支持按照端口或监听器名称进行模糊查询，该参数不能与ListenerName和Port同时使用"
      }
    ],
    "desc": "该接口（DescribeTCPListeners）用于查询单通道或者通道组下的TCP监听器信息。"
  },
  "DescribeDomainErrorPageInfo": {
    "params": [
      {
        "name": "ListenerId",
        "desc": "监听器ID"
      },
      {
        "name": "Domain",
        "desc": "域名"
      }
    ],
    "desc": "查询目前定制域名的错误响应"
  },
  "DescribeRealServers": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "查询源站的所属项目ID，-1表示所有项目"
      },
      {
        "name": "SearchValue",
        "desc": "需要查询的源站IP或域名，支持模糊匹配"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认值是0"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20个，最大值为50个"
      },
      {
        "name": "TagSet",
        "desc": "标签列表，当存在该字段时，拉取对应标签下的资源列表。\n最多支持5个标签，当存在两个或两个以上的标签时，满足其中任意一个标签时，源站会被拉取出来。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件。filter的name取值(RealServerName,RealServerIP)"
      }
    ],
    "desc": "本接口（DescribeRealServers）用于查询源站信息，可以根据项目名查询所有的源站信息，此外支持指定IP机或者域名的源站模糊查询。"
  },
  "DescribeDomainErrorPageInfoByIds": {
    "params": [
      {
        "name": "ErrorPageIds",
        "desc": "定制错误ID列表,最多支持10个"
      }
    ],
    "desc": "根据定制错误ID查询错误响应"
  },
  "ModifyUDPListenerAttribute": {
    "params": [
      {
        "name": "ListenerId",
        "desc": "监听器ID"
      },
      {
        "name": "GroupId",
        "desc": "通道组ID，ProxyId和GroupId必须设置一个，但不能同时设置。"
      },
      {
        "name": "ProxyId",
        "desc": "通道ID，ProxyId和GroupId必须设置一个，但不能同时设置。"
      },
      {
        "name": "ListenerName",
        "desc": "监听器名称"
      },
      {
        "name": "Scheduler",
        "desc": "监听器源站调度策略"
      }
    ],
    "desc": "本接口（ModifyUDPListenerAttribute）用于修改通道实例下UDP监听器配置，包括监听器名称和调度策略的修改。"
  },
  "DescribeProxyAndStatisticsListeners": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "项目ID"
      }
    ],
    "desc": "该接口为内部接口，用于查询可以获取统计数据的通道和监听器信息"
  },
  "CreateHTTPListener": {
    "params": [
      {
        "name": "ListenerName",
        "desc": "监听器名称"
      },
      {
        "name": "Port",
        "desc": "监听器端口，基于同种传输层协议（TCP 或 UDP）的监听器，端口不可重复"
      },
      {
        "name": "ProxyId",
        "desc": "通道ID，与GroupId不能同时设置，对应为通道创建监听器"
      },
      {
        "name": "GroupId",
        "desc": "通道组ID，与ProxyId不能同时设置，对应为通道组创建监听器"
      }
    ],
    "desc": "该接口（CreateHTTPListener）用于在通道实例下创建HTTP协议类型的监听器。"
  },
  "DescribeUDPListeners": {
    "params": [
      {
        "name": "ProxyId",
        "desc": "过滤条件，根据通道ID进行拉取，ProxyId/GroupId/ListenerId必须设置一个，但ProxyId和GroupId不能同时设置。"
      },
      {
        "name": "ListenerId",
        "desc": "过滤条件，根据监听器ID精确查询。\n当设置了ProxyId时，会检查该监听器是否归属于该通道。\n当设置了GroupId时，会检查该监听器是否归属于该通道组。"
      },
      {
        "name": "ListenerName",
        "desc": "过滤条件，根据监听器名称精确查询"
      },
      {
        "name": "Port",
        "desc": "过滤条件，根据监听器端口精确查询"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0"
      },
      {
        "name": "Limit",
        "desc": "限制数量，默认为20"
      },
      {
        "name": "GroupId",
        "desc": "过滤条件，根据通道组ID进行拉取，ProxyId/GroupId/ListenerId必须设置一个，但ProxyId和GroupId不能同时设置。"
      },
      {
        "name": "SearchValue",
        "desc": "过滤条件，支持按照端口或监听器名称进行模糊查询，该参数不能与ListenerName和Port同时使用"
      }
    ],
    "desc": "该接口（DescribeUDPListeners）用于查询单通道或者通道组下的UDP监听器信息"
  },
  "ModifyProxyConfiguration": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "（旧参数，请切换到ProxyId）通道的实例ID。"
      },
      {
        "name": "Bandwidth",
        "desc": "需要调整到的目标带宽，单位：Mbps。\nBandwidth与Concurrent必须至少设置一个。取值范围根据DescribeAccessRegionsByDestRegion接口获取得到"
      },
      {
        "name": "Concurrent",
        "desc": "需要调整到的目标并发值，单位：万。\nBandwidth与Concurrent必须至少设置一个。取值范围根据DescribeAccessRegionsByDestRegion接口获取得到"
      },
      {
        "name": "ClientToken",
        "desc": "用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。\n更多详细信息请参阅：如何保证幂等性。"
      },
      {
        "name": "ProxyId",
        "desc": "（新参数）通道的实例ID。"
      },
      {
        "name": "BillingType",
        "desc": "计费方式 (0:按带宽计费，1:按流量计费 默认按带宽计费）"
      }
    ],
    "desc": "本接口（ModifyProxyConfiguration）用于修改通道的配置。根据当前业务的容量需求，扩容或缩容相关通道的配置。仅支持Scalarable为1的通道,Scalarable可通过接口DescribeProxies获取。"
  },
  "CloseProxyGroup": {
    "params": [
      {
        "name": "GroupId",
        "desc": "通道组的实例 ID。"
      }
    ],
    "desc": "本接口（CloseProxyGroup）用于关闭通道组。通道组关闭后，不再产生流量，但每天仍然收取通道基础配置费用。"
  },
  "ModifyTCPListenerAttribute": {
    "params": [
      {
        "name": "ListenerId",
        "desc": "监听器ID"
      },
      {
        "name": "GroupId",
        "desc": "通道组ID，ProxyId和GroupId必须设置一个，但不能同时设置。"
      },
      {
        "name": "ProxyId",
        "desc": "通道ID，ProxyId和GroupId必须设置一个，但不能同时设置。"
      },
      {
        "name": "ListenerName",
        "desc": "监听器名称"
      },
      {
        "name": "Scheduler",
        "desc": "监听器源站调度策略，支持轮询（rr），加权轮询（wrr），最小连接数（lc）。"
      },
      {
        "name": "DelayLoop",
        "desc": "源站健康检查时间间隔，单位：秒。时间间隔取值在[5，300]之间。"
      },
      {
        "name": "ConnectTimeout",
        "desc": "源站健康检查响应超时时间，单位：秒。超时时间取值在[2，60]之间。超时时间应小于健康检查时间间隔DelayLoop。"
      },
      {
        "name": "HealthCheck",
        "desc": "是否开启健康检查，1开启，0关闭。"
      }
    ],
    "desc": "本接口（ModifyTCPListenerAttribute）用于修改通道实例下TCP监听器配置，包括健康检查的配置，调度策略。"
  },
  "ModifyProxyGroupAttribute": {
    "params": [
      {
        "name": "GroupId",
        "desc": "需要修改的通道组ID。"
      },
      {
        "name": "GroupName",
        "desc": "修改后的通道组名称：不超过30个字符，超过部分会被截断。"
      },
      {
        "name": "ProjectId",
        "desc": "项目ID"
      }
    ],
    "desc": "本接口（ModifyProxyGroupAttribute）用于修改通道组属性，目前仅支持修改通道组名称。"
  },
  "DescribeGroupAndStatisticsProxy": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "项目ID"
      }
    ],
    "desc": "该接口为内部接口，用于查询可以获取统计数据的通道组和通道信息"
  },
  "DescribeRealServerStatistics": {
    "params": [
      {
        "name": "RealServerId",
        "desc": "源站ID"
      },
      {
        "name": "ListenerId",
        "desc": "监听器ID"
      },
      {
        "name": "WithinTime",
        "desc": "统计时长，单位：小时。仅支持最近1,3,6,12,24小时的统计查询"
      },
      {
        "name": "RuleId",
        "desc": "规则ID"
      }
    ],
    "desc": "该接口（DescribeRealServerStatistics）用于查询源站健康检查结果的统计数据。源站状态展示位为1：正常或者0：异常。查询的源站需要在监听器或者规则上进行了绑定，查询时需指定绑定的监听器或者规则ID。该接口支持最近1，3，6，12，24小时内1分钟细粒度的源站状态统计数据展示。"
  },
  "BindListenerRealServers": {
    "params": [
      {
        "name": "ListenerId",
        "desc": "监听器ID"
      },
      {
        "name": "RealServerBindSet",
        "desc": "待绑定源站列表。如果该监听器的源站调度策略是加权轮询，需要填写源站权重 RealServerWeight, 不填或者其他调度类型默认源站权重为1。"
      }
    ],
    "desc": "本接口（BindListenerRealServers）用于TCP/UDP监听器绑定解绑源站。\n注意：本接口会解绑之前绑定的源站，绑定本次调用所选择的源站。例如：原来绑定的源站为A，B，C，本次调用的选择绑定的源站为C，D，E，那么调用后所绑定的源站为C，D，E。"
  },
  "CreateProxyGroupDomain": {
    "params": [
      {
        "name": "GroupId",
        "desc": "需要开启域名的通道组ID。"
      }
    ],
    "desc": "本接口（CreateProxyGroupDomain）用于创建通道组域名，并开启域名解析。"
  },
  "CreateProxyGroup": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "通道组所属项目ID"
      },
      {
        "name": "GroupName",
        "desc": "通道组别名"
      },
      {
        "name": "RealServerRegion",
        "desc": "源站地域，参考接口DescribeDestRegions 返回参数RegionDetail中的RegionId"
      },
      {
        "name": "TagSet",
        "desc": "标签列表"
      },
      {
        "name": "AccessRegionSet",
        "desc": "加速地域列表，包括加速地域名，及该地域对应的带宽和并发配置。"
      }
    ],
    "desc": "本接口（CreateProxyGroup）用于创建通道组。"
  },
  "CreateUDPListeners": {
    "params": [
      {
        "name": "ListenerName",
        "desc": "监听器名称"
      },
      {
        "name": "Ports",
        "desc": "监听器端口列表"
      },
      {
        "name": "Scheduler",
        "desc": "监听器源站调度策略，支持轮询（rr），加权轮询（wrr），最小连接数（lc）"
      },
      {
        "name": "RealServerType",
        "desc": "监听器对应源站类型，支持IP或者DOMAIN类型"
      },
      {
        "name": "ProxyId",
        "desc": "通道ID，ProxyId和GroupId必须设置一个，但不能同时设置。"
      },
      {
        "name": "GroupId",
        "desc": "通道组ID，ProxyId和GroupId必须设置一个，但不能同时设置。"
      },
      {
        "name": "RealServerPorts",
        "desc": "源站端口列表，该参数仅支持v1版本监听器和通道组监听器"
      }
    ],
    "desc": "该接口（CreateUDPListeners）用于批量创建单通道或者通道组的UDP协议类型的监听器。"
  },
  "DescribeRegionAndPrice": {
    "params": [],
    "desc": "该接口（DescribeRegionAndPrice）用于获取源站区域和带宽梯度价格"
  },
  "ModifySecurityRule": {
    "params": [
      {
        "name": "RuleId",
        "desc": "规则ID"
      },
      {
        "name": "AliasName",
        "desc": "规则名：不得超过30个字符，超过部分会被截断。"
      },
      {
        "name": "PolicyId",
        "desc": "安全策略ID"
      }
    ],
    "desc": "修改安全策略规则名"
  },
  "DescribeProxyDetail": {
    "params": [
      {
        "name": "ProxyId",
        "desc": "需查询的通道ID。"
      }
    ],
    "desc": "本接口（DescribeProxyDetail）用于查询通道详情。"
  },
  "DescribeListenerStatistics": {
    "params": [
      {
        "name": "ListenerId",
        "desc": "监听器ID"
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
        "name": "MetricNames",
        "desc": "统计指标名称列表，支持: 入带宽:InBandwidth, 出带宽:OutBandwidth, 并发:Concurrent, 入包量:InPackets, 出包量:OutPackets。"
      },
      {
        "name": "Granularity",
        "desc": "监控粒度，目前支持300，3600，86400，单位：秒。\n查询时间范围不超过1天，支持最小粒度300秒；\n查询间范围不超过7天，支持最小粒度3600秒；\n查询间范围超过7天，支持最小粒度86400秒。"
      }
    ],
    "desc": "该接口用于查询监听器统计数据，包括出入带宽，出入包量，并发数据。支持300秒, 3600秒和86400秒的细粒度，取值为细粒度范围内最大值。"
  },
  "DescribeRuleRealServers": {
    "params": [
      {
        "name": "RuleId",
        "desc": "转发规则ID"
      }
    ],
    "desc": "本接口（DescribeRuleRealServers）用于查询转发规则相关的源站信息， 包括该规则可绑定的源站信息和已绑定的源站信息。"
  },
  "AddRealServers": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "源站对应的项目ID"
      },
      {
        "name": "RealServerIP",
        "desc": "源站对应的IP或域名"
      },
      {
        "name": "RealServerName",
        "desc": "源站名称"
      },
      {
        "name": "TagSet",
        "desc": "标签列表"
      }
    ],
    "desc": "添加源站(服务器)信息，支持IP或域名"
  },
  "DescribeProxiesStatus": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "（旧参数，请切换到ProxyIds）通道ID列表。"
      },
      {
        "name": "ProxyIds",
        "desc": "（新参数）通道ID列表。"
      }
    ],
    "desc": "本接口（DescribeProxiesStatus）用于查询通道状态列表。"
  },
  "DescribeSecurityRules": {
    "params": [
      {
        "name": "SecurityRuleIds",
        "desc": "安全规则ID列表。总数不能超过20个。"
      }
    ],
    "desc": "本接口（DescribeSecurityRules）用于根据安全规则ID查询安全规则详情列表。支持一个或多个安全规则的查询。一次最多支持20个安全规则的查询。"
  },
  "DeleteDomain": {
    "params": [
      {
        "name": "ListenerId",
        "desc": "监听器ID"
      },
      {
        "name": "Domain",
        "desc": "需要删除的域名"
      },
      {
        "name": "Force",
        "desc": "是否强制删除已绑定源站的转发规则，0非强制，1强制。\n当采用非强制删除时，如果域名下已有规则绑定了源站，则无法删除。"
      }
    ],
    "desc": "本接口（DeleteDomain）仅适用于7层监听器，用于删除该监听器下对应域名及域名下的所有规则，所有已绑定源站的规则将自动解绑。"
  },
  "CreateCertificate": {
    "params": [
      {
        "name": "CertificateType",
        "desc": "证书类型。其中：\n0，表示基础认证配置；\n1，表示客户端CA证书；\n2，服务器SSL证书；\n3，表示源站CA证书；\n4，表示通道SSL证书。"
      },
      {
        "name": "CertificateContent",
        "desc": "证书内容。采用url编码。其中：\n当证书类型为基础认证配置时，该参数填写用户名/密码对。格式：“用户名：密码”，例如：root:FSGdT。其中密码使用htpasswd或者openssl，例如：openssl passwd -crypt 123456。\n当证书类型为CA/SSL证书时，该参数填写证书内容，格式为pem。"
      },
      {
        "name": "CertificateAlias",
        "desc": "证书名称"
      },
      {
        "name": "CertificateKey",
        "desc": "密钥内容。采用url编码。仅当证书类型为SSL证书时，需要填写该参数。格式为pem。"
      }
    ],
    "desc": "本接口（CreateCertificate）用于创建Gaap相关证书和配置文件，包括基础认证配置文件，客户端CA证书，服务器SSL证书，Gaap SSL证书以及源站CA证书。"
  },
  "CreateTCPListeners": {
    "params": [
      {
        "name": "ListenerName",
        "desc": "监听器名称。"
      },
      {
        "name": "Ports",
        "desc": "监听器端口列表。"
      },
      {
        "name": "Scheduler",
        "desc": "监听器源站调度策略，支持轮询（rr），加权轮询（wrr），最小连接数（lc）。"
      },
      {
        "name": "HealthCheck",
        "desc": "源站是否开启健康检查：1开启，0关闭，UDP监听器不支持健康检查"
      },
      {
        "name": "RealServerType",
        "desc": "监听器对应源站类型，支持IP或者DOMAIN类型。DOMAIN源站类型不支持wrr的源站调度策略。"
      },
      {
        "name": "ProxyId",
        "desc": "通道ID，ProxyId和GroupId必须设置一个，但不能同时设置。"
      },
      {
        "name": "GroupId",
        "desc": "通道组ID，ProxyId和GroupId必须设置一个，但不能同时设置。"
      },
      {
        "name": "DelayLoop",
        "desc": "源站健康检查时间间隔，单位：秒。时间间隔取值在[5，300]之间。"
      },
      {
        "name": "ConnectTimeout",
        "desc": "源站健康检查响应超时时间，单位：秒。超时时间取值在[2，60]之间。超时时间应小于健康检查时间间隔DelayLoop。"
      },
      {
        "name": "RealServerPorts",
        "desc": "源站端口列表，该参数仅支持v1版本监听器和通道组监听器。"
      }
    ],
    "desc": "该接口（CreateTCPListeners）用于批量创建单通道或者通道组的TCP协议类型的监听器。"
  },
  "DescribeRules": {
    "params": [
      {
        "name": "ListenerId",
        "desc": "7层监听器Id。"
      }
    ],
    "desc": "本接口（DescribeRules）用于查询监听器下的所有规则信息，包括规则域名，路径以及该规则下所绑定的源站列表。当通道版本为3.0时，该接口会返回该域名对应的高级认证配置信息。"
  },
  "ModifyProxiesAttribute": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "（旧参数，请切换到ProxyIds）一个或多个待操作的通道ID。"
      },
      {
        "name": "ProxyName",
        "desc": "通道名称。可任意命名，但不得超过30个字符。"
      },
      {
        "name": "ClientToken",
        "desc": "用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。\n更多详细信息请参阅：如何保证幂等性。"
      },
      {
        "name": "ProxyIds",
        "desc": "（新参数）一个或多个待操作的通道ID。"
      }
    ],
    "desc": "本接口（ModifyProxiesAttribute）用于修改实例的属性（目前只支持修改通道的名称）。"
  },
  "DestroyProxies": {
    "params": [
      {
        "name": "Force",
        "desc": "强制删除标识。\n1，强制删除该通道列表，无论是否已经绑定了源站；\n0，如果已绑定了源站，则无法删除。\n删除多通道时，如果该标识为0，只有所有的通道都没有绑定源站，才允许删除。"
      },
      {
        "name": "InstanceIds",
        "desc": "（旧参数，请切换到ProxyIds）通道实例ID列表。"
      },
      {
        "name": "ClientToken",
        "desc": "用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。\n更多详细信息请参阅：如何保证幂等性。"
      },
      {
        "name": "ProxyIds",
        "desc": "（新参数）通道实例ID列表。"
      }
    ],
    "desc": "本接口（DestroyProxies）用于销毁。通道销毁后，不再产生任何费用。"
  },
  "DescribeResourcesByTag": {
    "params": [
      {
        "name": "TagKey",
        "desc": "标签键。"
      },
      {
        "name": "TagValue",
        "desc": "标签值。"
      },
      {
        "name": "ResourceType",
        "desc": "资源类型，其中：\nProxy表示通道；\nProxyGroup表示通道组；\nRealServer表示源站。\n不指定该字段则查询该标签下所有资源。"
      }
    ],
    "desc": "本接口（DescribeResourcesByTag）用于根据标签来查询对应的资源信息，包括通道，通道组和源站。"
  },
  "DescribeCountryAreaMapping": {
    "params": [],
    "desc": "本接口（DescribeCountryAreaMapping）用于获取国家地区编码映射表。"
  },
  "DescribeListenerRealServers": {
    "params": [
      {
        "name": "ListenerId",
        "desc": "监听器ID"
      }
    ],
    "desc": "该接口（DescribeListenerRealServers）用于查询TCP/UDP监听器源站列表，包括该监听器已经绑定的源站列表以及可以绑定的源站列表。"
  },
  "DeleteListeners": {
    "params": [
      {
        "name": "ListenerIds",
        "desc": "待删除的监听器ID列表"
      },
      {
        "name": "Force",
        "desc": "已绑定源站的监听器是否允许强制删除，1：允许， 0：不允许"
      },
      {
        "name": "GroupId",
        "desc": "通道组ID，该参数和GroupId必须设置一个，但不能同时设置。"
      },
      {
        "name": "ProxyId",
        "desc": "通道ID，该参数和GroupId必须设置一个，但不能同时设置。"
      }
    ],
    "desc": "该接口（DeleteListeners）用于批量删除通道或通道组的监听器，包括4/7层监听器。"
  },
  "DescribeRealServersStatus": {
    "params": [
      {
        "name": "RealServerIds",
        "desc": "源站ID列表"
      }
    ],
    "desc": "本接口（DescribeRealServersStatus）用于查询源站是否已被规则或者监听器绑定"
  },
  "DescribeRulesByRuleIds": {
    "params": [
      {
        "name": "RuleIds",
        "desc": "规则ID列表。最多支持10个规则。"
      }
    ],
    "desc": "本接口（DescribeRulesByRuleIds）用于根据规则ID拉取规则信息列表。支持一个或者多个规则信息的拉取。一次最多支持10个规则信息的拉取。"
  },
  "InquiryPriceCreateProxy": {
    "params": [
      {
        "name": "AccessRegion",
        "desc": "加速区域名称。"
      },
      {
        "name": "Bandwidth",
        "desc": "通道带宽上限，单位：Mbps。"
      },
      {
        "name": "DestRegion",
        "desc": "（旧参数，请切换到RealServerRegion）源站区域名称。"
      },
      {
        "name": "Concurrency",
        "desc": "（旧参数，请切换到Concurrent）通道并发量上限，表示同时在线的连接数，单位：万。"
      },
      {
        "name": "RealServerRegion",
        "desc": "（新参数）源站区域名称。"
      },
      {
        "name": "Concurrent",
        "desc": "（新参数）通道并发量上限，表示同时在线的连接数，单位：万。"
      },
      {
        "name": "BillingType",
        "desc": "计费方式，0表示按带宽计费，1表示按流量计费。默认按带宽计费"
      }
    ],
    "desc": "本接口（InquiryPriceCreateProxy）用于创建加速通道询价。"
  }
}