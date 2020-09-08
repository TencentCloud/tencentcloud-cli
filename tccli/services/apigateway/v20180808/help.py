# -*- coding: utf-8 -*-
DESC = "apigateway-2018-08-08"
INFO = {
  "CreateService": {
    "params": [
      {
        "name": "ServiceName",
        "desc": "用户自定义的服务名称。如果没传，则系统自动生成一个唯一名称。"
      },
      {
        "name": "Protocol",
        "desc": "服务的前端请求类型。如 http、https、http&https。"
      },
      {
        "name": "ServiceDesc",
        "desc": "用户自定义的服务描述。"
      },
      {
        "name": "ExclusiveSetName",
        "desc": "独立集群名称，用于指定创建服务所在的独立集群。"
      },
      {
        "name": "NetTypes",
        "desc": "网络类型列表，用于指定支持的访问类型，INNER为内网访问，OUTER为外网访问。默认为OUTER。"
      },
      {
        "name": "IpVersion",
        "desc": "IP版本号，支持IPv4和IPv6，默认为IPv4。"
      },
      {
        "name": "SetServerName",
        "desc": "集群名称。保留字段，tsf serverlss类型使用。"
      },
      {
        "name": "AppIdType",
        "desc": "用户类型。保留类型，serverless用户使用。"
      }
    ],
    "desc": "本接口（CreateService）用于创建服务。\nAPI 网关使用的最大单元为服务，每个服务中可创建多个 API 接口。每个服务有一个默认域名供客户调用，用户也可绑定自定义域名到此服务中。"
  },
  "DescribeUsagePlansStatus": {
    "params": [
      {
        "name": "Limit",
        "desc": "返回数量，默认为 20，最大值为 100。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为 0。"
      },
      {
        "name": "Filters",
        "desc": "使用计划过滤条件。支持UsagePlanId、UsagePlanName、NotServiceId、NotApiId、Environment。"
      }
    ],
    "desc": "本接口（DescribeUsagePlanStatus）用于查询使用计划的列表。"
  },
  "DeleteUsagePlan": {
    "params": [
      {
        "name": "UsagePlanId",
        "desc": "待删除的使用计划唯一 ID。"
      }
    ],
    "desc": "本接口（DeleteUsagePlan）用于删除使用计划。"
  },
  "ModifyApi": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "API 所在的服务唯一 ID。"
      },
      {
        "name": "ServiceType",
        "desc": "API 的后端服务类型。支持HTTP、MOCK、TSF、CLB、SCF、WEBSOCKET、TARGET（内测）。"
      },
      {
        "name": "RequestConfig",
        "desc": "请求的前端配置。"
      },
      {
        "name": "ApiId",
        "desc": "API 接口唯一 ID。"
      },
      {
        "name": "ApiName",
        "desc": "用户自定义的 API 名称。"
      },
      {
        "name": "ApiDesc",
        "desc": "用户自定义的 API 接口描述。"
      },
      {
        "name": "ApiType",
        "desc": "API 类型，支持NORMAL和TSF，默认为NORMAL。"
      },
      {
        "name": "AuthType",
        "desc": "API 鉴权类型。支持SECRET、NONE、OAUTH。默认为NONE。"
      },
      {
        "name": "AuthRequired",
        "desc": "是否需要签名认证，True 表示需要，False 表示不需要。待废弃。"
      },
      {
        "name": "ServiceTimeout",
        "desc": "API 的后端服务超时时间，单位是秒。"
      },
      {
        "name": "Protocol",
        "desc": "API 的前端请求类型，如 HTTP 或 HTTPS 或者 HTTP 和 HTTPS。"
      },
      {
        "name": "EnableCORS",
        "desc": "是否需要开启跨域，Ture 表示需要，False 表示不需要。"
      },
      {
        "name": "ConstantParameters",
        "desc": "常量参数。"
      },
      {
        "name": "RequestParameters",
        "desc": "前端请求参数。"
      },
      {
        "name": "ApiBusinessType",
        "desc": "当AuthType 为 OAUTH时，该字段有效， NORMAL：业务api   OAUTH：授权API。"
      },
      {
        "name": "ServiceMockReturnMessage",
        "desc": "API 的后端 Mock 返回信息。如果 ServiceType 是 Mock，则此参数必传。"
      },
      {
        "name": "MicroServices",
        "desc": "API绑定微服务服务列表。"
      },
      {
        "name": "ServiceTsfLoadBalanceConf",
        "desc": "微服务的负载均衡配置。"
      },
      {
        "name": "ServiceTsfHealthCheckConf",
        "desc": "微服务的健康检查配置。"
      },
      {
        "name": "TargetServicesLoadBalanceConf",
        "desc": "target类型负载均衡配置。（内测阶段）"
      },
      {
        "name": "TargetServicesHealthCheckConf",
        "desc": "target健康检查配置。（内测阶段）"
      },
      {
        "name": "ServiceScfFunctionName",
        "desc": "scf 函数名称。当后端类型是SCF时生效。"
      },
      {
        "name": "ServiceWebsocketRegisterFunctionName",
        "desc": "scf websocket注册函数。当前端类型是WEBSOCKET且后端类型是SCF时生效。"
      },
      {
        "name": "ServiceWebsocketCleanupFunctionName",
        "desc": "scf websocket清理函数。当前端类型是WEBSOCKET且后端类型是SCF时生效。"
      },
      {
        "name": "ServiceWebsocketTransportFunctionName",
        "desc": "scf websocket传输函数。当前端类型是WEBSOCKET且后端类型是SCF时生效。"
      },
      {
        "name": "ServiceScfFunctionNamespace",
        "desc": "scf 函数命名空间。当后端类型是SCF时生效。"
      },
      {
        "name": "ServiceScfFunctionQualifier",
        "desc": "scf函数版本。当后端类型是SCF时生效。"
      },
      {
        "name": "ServiceWebsocketRegisterFunctionNamespace",
        "desc": "scf websocket注册函数命名空间。当前端类型是WEBSOCKET且后端类型是SCF时生效。"
      },
      {
        "name": "ServiceWebsocketRegisterFunctionQualifier",
        "desc": "scf websocket传输函数版本。当前端类型是WEBSOCKET且后端类型是SCF时生效。"
      },
      {
        "name": "ServiceWebsocketTransportFunctionNamespace",
        "desc": "scf websocket传输函数命名空间。当前端类型是WEBSOCKET且后端类型是SCF时生效。"
      },
      {
        "name": "ServiceWebsocketTransportFunctionQualifier",
        "desc": "scf websocket传输函数版本。当前端类型是WEBSOCKET且后端类型是SCF时生效。"
      },
      {
        "name": "ServiceWebsocketCleanupFunctionNamespace",
        "desc": "scf websocket清理函数命名空间。当前端类型是WEBSOCKET且后端类型是SCF时生效。"
      },
      {
        "name": "ServiceWebsocketCleanupFunctionQualifier",
        "desc": "scf websocket清理函数版本。当前端类型是WEBSOCKET且后端类型是SCF时生效。"
      },
      {
        "name": "ServiceScfIsIntegratedResponse",
        "desc": "是否开启响应集成。当后端类型是SCF时生效。"
      },
      {
        "name": "IsDebugAfterCharge",
        "desc": "开始调试后计费。（云市场预留字段）"
      },
      {
        "name": "TagSpecifications",
        "desc": "标签。"
      },
      {
        "name": "IsDeleteResponseErrorCodes",
        "desc": "是否删除自定义响应配置错误码，如果不传或者传 False，不删除，当传 True 时，则删除此 API 所有自定义响应配置错误码。"
      },
      {
        "name": "ResponseType",
        "desc": "返回类型。"
      },
      {
        "name": "ResponseSuccessExample",
        "desc": "自定义响应配置成功响应示例。"
      },
      {
        "name": "ResponseFailExample",
        "desc": "自定义响应配置失败响应示例。"
      },
      {
        "name": "ServiceConfig",
        "desc": "API 的后端服务配置。"
      },
      {
        "name": "AuthRelationApiId",
        "desc": "关联的授权API 唯一 ID，当AuthType为OAUTH且ApiBusinessType为NORMAL时生效。标示业务API绑定的oauth2.0授权API唯一ID。"
      },
      {
        "name": "ServiceParameters",
        "desc": "API的后端服务参数。"
      },
      {
        "name": "OauthConfig",
        "desc": "oauth配置。当AuthType是OAUTH时生效。"
      },
      {
        "name": "ResponseErrorCodes",
        "desc": "用户自定义错误码配置。"
      }
    ],
    "desc": "本接口（ModifyApi）用于修改 API 接口，可调用此接口对已经配置的 API 接口进行编辑修改。修改后的 API 需要重新发布 API 所在的服务到对应环境方能生效。"
  },
  "DemoteServiceUsagePlan": {
    "params": [
      {
        "name": "UsagePlanId",
        "desc": "使用计划ID。"
      },
      {
        "name": "ServiceId",
        "desc": "待降级的服务唯一 ID。"
      },
      {
        "name": "Environment",
        "desc": "环境名称。"
      }
    ],
    "desc": "本接口（DemoteServiceUsagePlan）用于将某个服务在某个环境的使用计划，降级到API上。\n如果服务内没有API不允许进行此操作。\n如果当前环境没有发布，不允许进行此操作。"
  },
  "DescribeApiKeysStatus": {
    "params": [
      {
        "name": "Limit",
        "desc": "返回数量，默认为 20，最大值为 100。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为 0。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件。支持AccessKeyId、AccessKeySecret、SecretName、NotUsagePlanId、Status、KeyWord（ 可以匹配name或者path）。"
      }
    ],
    "desc": "本接口（DescribeApiKeysStatus）用于查询密钥列表。\n当用户创建了多个密钥对时，可使用本接口查询一个或多个 API 密钥信息，本接口不会显示密钥 Key。"
  },
  "ModifyApiEnvironmentStrategy": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "服务唯一ID。"
      },
      {
        "name": "Strategy",
        "desc": "限流值。"
      },
      {
        "name": "EnvironmentName",
        "desc": "环境名。"
      },
      {
        "name": "ApiIds",
        "desc": "API列表。"
      }
    ],
    "desc": "本接口（ModifyApiEnvironmentStrategy）用于修改API限流策略"
  },
  "DescribeLogSearch": {
    "params": [
      {
        "name": "StartTime",
        "desc": "日志开始时间"
      },
      {
        "name": "EndTime",
        "desc": "日志结束时间"
      },
      {
        "name": "ServiceId",
        "desc": "服务id"
      },
      {
        "name": "Filters",
        "desc": "保留字段"
      },
      {
        "name": "Limit",
        "desc": "单次要返回的日志条数，单次返回的最大条数为100"
      },
      {
        "name": "ConText",
        "desc": "根据上次返回的ConText，获取后续的内容，最多可获取10000条"
      },
      {
        "name": "Sort",
        "desc": "按时间排序 asc（升序）或者 desc（降序），默认为 desc"
      },
      {
        "name": "Query",
        "desc": "保留字段"
      },
      {
        "name": "LogQuerys",
        "desc": "检索条件,支持的检索条件如下：\nreq_id：“=”\napi_id：“=”\ncip：“=”\nuip：“:”\nerr_msg：“:”\nrsp_st：“=” 、“!=” 、 “:” 、 “>” 、 “<”\nreq_t：”>=“ 、 ”<=“\n\n说明：\n“:”表示包含，“!=”表示不等于，字段含义见输出参数的LogSet说明"
      }
    ],
    "desc": "本接口DescribeLogSearch用于搜索日志"
  },
  "DescribeUsagePlanSecretIds": {
    "params": [
      {
        "name": "UsagePlanId",
        "desc": "绑定的使用计划唯一 ID。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为 20，最大值为 100。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为 0。"
      }
    ],
    "desc": "本接口（DescribeUsagePlanSecretIds）用于查询使用计划绑定的密钥列表。\n在 API 网关中，一个使用计划可绑定多个密钥对，可使用本接口查询使用计划绑定的密钥列表。"
  },
  "DescribeServiceSubDomains": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "服务唯一 ID。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为 20，最大值为 100。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为 0。"
      }
    ],
    "desc": "本接口（DescribeServiceSubDomains）用于查询自定义域名列表。\nAPI 网关可绑定自定义域名到服务，用于服务调用。此接口用于查询用户绑定在服务的自定义域名列表。"
  },
  "DescribeService": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "待查询的服务唯一 ID。"
      }
    ],
    "desc": "本接口（DescribeService）用于查询一个服务的详细信息、包括服务的描述、域名、协议、创建时间、发布情况等信息。"
  },
  "ModifyIPStrategy": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "待修改的策略所属服务的唯一ID。"
      },
      {
        "name": "StrategyId",
        "desc": "待修改的策略唯一ID。"
      },
      {
        "name": "StrategyData",
        "desc": "待修改的策略详情。"
      }
    ],
    "desc": "本接口（ModifyIPStrategy）用于修改服务IP策略。"
  },
  "DeleteService": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "待删除服务的唯一 ID。"
      }
    ],
    "desc": "本接口（DeleteService）用于删除 API 网关中某个服务。"
  },
  "UpdateService": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "待切换服务的唯一 Id。"
      },
      {
        "name": "EnvironmentName",
        "desc": "待切换的环境名称，当前支持三个环境，test（测试环境）、prepub（预发布环境）和 release（发布环境）。"
      },
      {
        "name": "VersionName",
        "desc": "切换的版本号。"
      },
      {
        "name": "UpdateDesc",
        "desc": "本次的切换描述。"
      }
    ],
    "desc": "本接口（UpdateService）用于从服务发布的环境中运行版本切换到特定版本。用户在使用 API 网关创建服务并发布服务到某个环境后，多因为开发过程会产生多个版本，此时可调用本接口。"
  },
  "DescribeIPStrategyApisStatus": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "服务唯一ID。"
      },
      {
        "name": "StrategyId",
        "desc": "策略唯一ID。"
      },
      {
        "name": "EnvironmentName",
        "desc": "策略所在环境。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为 20，最大值为 100。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为 0。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件。支持 ApiPath、ApiName、KeyWord（模糊查询Path 和Name）。"
      }
    ],
    "desc": "本接口（DescribeIPStrategyApisStatus）用于查询IP策略可以绑定的API列表。即服务下所有API和该策略已绑定API的差集。"
  },
  "UnReleaseService": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "待下线服务的唯一 ID。"
      },
      {
        "name": "EnvironmentName",
        "desc": "待下线的环境名称，当前支持三个环境，test（测试环境）、prepub（预发布环境）和 release（发布环境）。"
      },
      {
        "name": "ApiIds",
        "desc": "保留字段，待下线的API列表。"
      }
    ],
    "desc": "本接口（UnReleaseService）用于下线服务。\n用户发布服务到某个环境后，此服务中的 API 方可被调用者进行调用，当用户需要将此服务从发布环境中下线时，可调用此 API。下线后的服务不可被调用。"
  },
  "ModifyApiIncrement": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "服务ID"
      },
      {
        "name": "ApiId",
        "desc": "接口ID"
      },
      {
        "name": "BusinessType",
        "desc": "需要修改的API auth类型(可选择OAUTH-授权API)"
      },
      {
        "name": "PublicKey",
        "desc": "oauth接口需要修改的公钥值"
      },
      {
        "name": "LoginRedirectUrl",
        "desc": "oauth接口重定向地址"
      }
    ],
    "desc": "提供增量更新API能力，主要是给程序调用（区别于ModifyApi，该接口是需要传入API的全量参数，对console使用较友好）"
  },
  "DescribeServiceEnvironmentReleaseHistory": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "待查询的服务唯一 ID。"
      },
      {
        "name": "EnvironmentName",
        "desc": "环境名称。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为 20，最大值为 100。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为 0。"
      }
    ],
    "desc": "本接口（DescribeServiceEnvironmentReleaseHistory）用于查询服务环境的发布历史。\n用户在创建好服务后需要发布到某个环境中才能进行使用，本接口用于查询一个服务某个环境的发布记录。"
  },
  "DescribeApiUsagePlan": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "待查询的服务唯一 ID。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为 20，最大值为 100。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为 0。"
      }
    ],
    "desc": "本接口（DescribeApiUsagePlan）用于查询服务中 API 使用计划详情。\n服务若需要鉴权限流生效，则需要绑定使用计划到此服务中，本接口用于查询绑定到一个服务及其中 API 的所有使用计划。"
  },
  "DeleteApi": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "API 所在的服务唯一 ID。"
      },
      {
        "name": "ApiId",
        "desc": "API 接口唯一 ID。"
      }
    ],
    "desc": "本接口（DeleteApi）用于删除已经创建的API。"
  },
  "DescribeIPStrategysStatus": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "服务唯一ID。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件。支持StrategyName。"
      }
    ],
    "desc": "本接口（DescribeIPStrategysStatus）用于查询服务IP策略列表。"
  },
  "DescribeServiceUsagePlan": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "待查询的服务唯一 ID。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      }
    ],
    "desc": "本接口（DescribeServiceUsagePlan）用于查询服务使用计划详情。\n服务若需要鉴权限流生效，则需要绑定使用计划到此服务中，本接口用于查询绑定到一个服务的所有使用计划。"
  },
  "ModifyServiceEnvironmentStrategy": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "服务的唯一ID。"
      },
      {
        "name": "Strategy",
        "desc": "限流值。"
      },
      {
        "name": "EnvironmentNames",
        "desc": "环境列表。"
      }
    ],
    "desc": "本接口（ModifyServiceEnvironmentStrategy）用于修改服务限流策略"
  },
  "CreateUsagePlan": {
    "params": [
      {
        "name": "UsagePlanName",
        "desc": "用户自定义的使用计划名称。"
      },
      {
        "name": "UsagePlanDesc",
        "desc": "用户自定义的使用计划描述。"
      },
      {
        "name": "MaxRequestNum",
        "desc": "请求配额总数，取值范围为-1或者[1, 99999999]，默认为-1，表示不开启。"
      },
      {
        "name": "MaxRequestNumPreSec",
        "desc": "每秒请求限制数，取值范围为-1或者[1, 2000]，默认-1，表示不开启。"
      }
    ],
    "desc": "本接口（CreateUsagePlan）用于创建使用计划。\n用户在使用 API 网关时，需要创建使用计划并将其绑定到服务的环境中使用。"
  },
  "DeleteApiKey": {
    "params": [
      {
        "name": "AccessKeyId",
        "desc": "待删除的密钥 ID。"
      }
    ],
    "desc": "本接口（DeleteApiKey）用于删除一对 API 密钥。"
  },
  "ModifyService": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "待修改服务的唯一 Id。"
      },
      {
        "name": "ServiceName",
        "desc": "修改后的服务名称。"
      },
      {
        "name": "ServiceDesc",
        "desc": "修改后的服务描述。"
      },
      {
        "name": "Protocol",
        "desc": "修改后的服务前端请求类型，如 http、https和 http&https。"
      },
      {
        "name": "NetTypes",
        "desc": "网络类型列表，用于指定支持的访问类型，INNER为内网访问，OUTER为外网访问。默认为OUTER。"
      }
    ],
    "desc": "本接口（ModifyService）用于修改服务的相关信息。当服务创建后，服务的名称、描述和服务类型均可被修改。"
  },
  "UpdateApiKey": {
    "params": [
      {
        "name": "AccessKeyId",
        "desc": "待更换的密钥 ID。"
      },
      {
        "name": "AccessKeySecret",
        "desc": "待更换的密钥 Key，更新自定义密钥时，该字段为必传。长度10 - 50字符，包括字母、数字、英文下划线。"
      }
    ],
    "desc": "本接口（UpdateApiKey）用于更换用户已创建的一对 API 密钥。"
  },
  "ModifyUsagePlan": {
    "params": [
      {
        "name": "UsagePlanId",
        "desc": "使用计划唯一 ID。"
      },
      {
        "name": "UsagePlanName",
        "desc": "修改后的用户自定义的使用计划名称。"
      },
      {
        "name": "UsagePlanDesc",
        "desc": "修改后的用户自定义的使用计划描述。"
      },
      {
        "name": "MaxRequestNum",
        "desc": "请求配额总数，取值范围为-1或者[1, 99999999]，默认为-1，表示不开启。"
      },
      {
        "name": "MaxRequestNumPreSec",
        "desc": "每秒请求限制数，取值范围为-1或者[1, 2000]，默认-1，表示不开启。"
      }
    ],
    "desc": "本接口（ModifyUsagePlan）用于修改使用计划的名称，描述及 QPS。"
  },
  "BindEnvironment": {
    "params": [
      {
        "name": "UsagePlanIds",
        "desc": "待绑定的使用计划唯一 ID 列表。"
      },
      {
        "name": "BindType",
        "desc": "绑定类型，取值为API、SERVICE，默认值为SERVICE。"
      },
      {
        "name": "Environment",
        "desc": "待绑定的环境。"
      },
      {
        "name": "ServiceId",
        "desc": "待绑定的服务唯一 ID。"
      },
      {
        "name": "ApiIds",
        "desc": "API唯一ID数组，当bindType=API时，需要传入此参数。"
      }
    ],
    "desc": "本接口（BindEnvironment）用于绑定使用计划到服务或API。\n用户在发布服务到某个环境中后，如果 API 需要鉴权，还需要绑定使用计划才能进行调用，此接口用户将使用计划绑定到特定环境。\n目前支持绑定使用计划到API，但是同一个服务不能同时存在绑定到服务的使用计划和绑定到API的使用计划，所以对已经绑定过服务级别使用计划的环境，请先使用 服务级别使用计划降级 接口进行降级操作。"
  },
  "UnBindSecretIds": {
    "params": [
      {
        "name": "UsagePlanId",
        "desc": "待解绑的使用计划唯一 ID。"
      },
      {
        "name": "AccessKeyIds",
        "desc": "待解绑的密钥 ID 数组。"
      }
    ],
    "desc": "本接口（UnBindSecretIds）用于为使用计划解绑密钥。"
  },
  "BindIPStrategy": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "待绑定的IP策略所属的服务唯一ID。"
      },
      {
        "name": "StrategyId",
        "desc": "待绑定的IP策略唯一ID。"
      },
      {
        "name": "EnvironmentName",
        "desc": "IP策略待绑定的环境。"
      },
      {
        "name": "BindApiIds",
        "desc": "IP策略待绑定的API列表。"
      }
    ],
    "desc": "本接口（BindIPStrategy）用于API绑定IP策略。"
  },
  "UnBindIPStrategy": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "待解绑的服务唯一ID。"
      },
      {
        "name": "StrategyId",
        "desc": "待解绑的IP策略唯一ID。"
      },
      {
        "name": "EnvironmentName",
        "desc": "待解绑的环境。"
      },
      {
        "name": "UnBindApiIds",
        "desc": "待解绑的 API 列表。"
      }
    ],
    "desc": "本接口（UnBindIPStrategy）用于服务解绑IP策略。"
  },
  "DescribeIPStrategy": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "服务唯一ID。"
      },
      {
        "name": "StrategyId",
        "desc": "IP 策略唯一ID。"
      },
      {
        "name": "EnvironmentName",
        "desc": "策略关联的环境。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为 20，最大值为 100。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为 0。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件。预留字段，目前不支持过滤。"
      }
    ],
    "desc": "本接口（DescribeIPStrategy）用于查询IP策略详情。"
  },
  "DescribeUsagePlanEnvironments": {
    "params": [
      {
        "name": "UsagePlanId",
        "desc": "待查询的使用计划唯一 ID。"
      },
      {
        "name": "BindType",
        "desc": "定类型，取值为 API、SERVICE，默认值为 SERVICE。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为 20，最大值为 100。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为 0。"
      }
    ],
    "desc": "本接口（DescribeUsagePlanEnvironments）用于查询使用计划绑定的环境列表。\n用户在绑定了某个使用计划到环境后，可使用本接口查询这个使用计划绑定的所有服务的环境。"
  },
  "EnableApiKey": {
    "params": [
      {
        "name": "AccessKeyId",
        "desc": "待启用的密钥 ID。"
      }
    ],
    "desc": "本接口（EnableApiKey）用于启动一对被禁用的 API 密钥。"
  },
  "CreateIPStrategy": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "服务的唯一ID。"
      },
      {
        "name": "StrategyName",
        "desc": "用户自定义的策略名称。"
      },
      {
        "name": "StrategyType",
        "desc": "策略类型。支持WHITE（白名单）和BLACK（黑名单）。"
      },
      {
        "name": "StrategyData",
        "desc": "策略详情。"
      }
    ],
    "desc": "本接口（CreateIPStrategy）用于创建服务IP策略。"
  },
  "DescribeServiceReleaseVersion": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "待查询的服务唯一 ID。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为 20，最大值为 100。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      }
    ],
    "desc": "本接口（DescribeServiceReleaseVersion）查询一个服务下面所有已经发布的版本列表。\n用户在发布服务时，常有多个版本发布，可使用本接口查询已发布的版本。"
  },
  "DescribeApisStatus": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "API 所在的服务唯一 ID。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为 0。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为 20，最大值为 100"
      },
      {
        "name": "Filters",
        "desc": "API过滤条件。支持ApiId、ApiName、ApiPath、ApiType、AuthRelationApiId、AuthType、ApiBuniessType、NotUsagePlanId、Environment、Tags (values为 $tag_key:tag_value的列表)、TagKeys （values 为 tag key的列表）。"
      }
    ],
    "desc": "本接口（DescribeApisStatus）用于查看一个服务下的某个 API 或所有 API 列表及其相关信息。"
  },
  "CreateApiKey": {
    "params": [
      {
        "name": "SecretName",
        "desc": "用户自定义密钥名称。"
      },
      {
        "name": "AccessKeyType",
        "desc": "密钥类型，支持 auto 和 manual（自定义密钥），默认为 auto。"
      },
      {
        "name": "AccessKeyId",
        "desc": "用户自定义密钥 ID，AccessKeyType 为 manual 时必传。长度为5 - 50字符，由字母、数字、英文下划线组成。"
      },
      {
        "name": "AccessKeySecret",
        "desc": "用户自定义密钥 Key，AccessKeyType 为 manual 时必传。长度为10 - 50字符，由字母、数字、英文下划线。"
      }
    ],
    "desc": "本接口（CreateApiKey）用于创建一对新的 API 密钥。"
  },
  "ModifySubDomain": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "服务唯一 ID。"
      },
      {
        "name": "SubDomain",
        "desc": "待修改路径映射的自定义的域名。"
      },
      {
        "name": "IsDefaultMapping",
        "desc": "是否修改为使用默认路径映射。为 true，表示使用默认路径映射，为 false，表示使用自定义路径映射。"
      },
      {
        "name": "CertificateId",
        "desc": "证书 ID，协议包含 HTTPS 的时候要传该字段。"
      },
      {
        "name": "Protocol",
        "desc": "修改后的自定义域名协议类型。（http，https 或 http&https)"
      },
      {
        "name": "PathMappingSet",
        "desc": "修改后的路径映射列表。"
      },
      {
        "name": "NetType",
        "desc": "网络类型 （'INNER' 或 'OUTER'）"
      }
    ],
    "desc": "本接口（ModifySubDomain）用于修改服务的自定义域名设置中的路径映射，可以修改绑定自定义域名之前的路径映射规则。"
  },
  "DescribeServiceEnvironmentList": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "待查询的服务唯一 ID。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为 20，最大值为 100。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为 0。"
      }
    ],
    "desc": "本接口（DescribeServiceEnvironmentList）用于查询一个服务的环境列表，可查询到此服务下所有环境及其状态。"
  },
  "DisableApiKey": {
    "params": [
      {
        "name": "AccessKeyId",
        "desc": "待禁用的密钥 ID。"
      }
    ],
    "desc": "本接口（DisableApiKey）用于禁用一对 API 密钥。"
  },
  "ReleaseService": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "待发布服务的唯一 ID。"
      },
      {
        "name": "EnvironmentName",
        "desc": "待发布的环境名称，当前支持三个环境，test（测试环境）、prepub（预发布环境）和 release（发布环境）。"
      },
      {
        "name": "ReleaseDesc",
        "desc": "本次的发布描述。"
      },
      {
        "name": "ApiIds",
        "desc": "apiId列表，预留字段，默认全量api发布。"
      }
    ],
    "desc": "本接口（ReleaseService）用于发布服务。\nAPI 网关的服务创建后，需要发布到某个环境方生效后，使用者才能进行调用，此接口用于发布服务到环境，如 release 环境。"
  },
  "UnBindEnvironment": {
    "params": [
      {
        "name": "BindType",
        "desc": "绑定类型，取值为 API、SERVICE，默认值为 SERVICE。"
      },
      {
        "name": "UsagePlanIds",
        "desc": "待绑定的使用计划唯一 ID 列表。"
      },
      {
        "name": "Environment",
        "desc": "待解绑的服务环境。"
      },
      {
        "name": "ServiceId",
        "desc": "待解绑的服务唯一 ID。"
      },
      {
        "name": "ApiIds",
        "desc": "API 唯一 ID 数组，当 BindType=API 时，需要传入此参数。"
      }
    ],
    "desc": "本接口（UnBindEnvironment）用于将使用计划从特定环境解绑。"
  },
  "DescribeApiEnvironmentStrategy": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "API所属服务唯一ID。"
      },
      {
        "name": "EnvironmentNames",
        "desc": "环境列表。"
      },
      {
        "name": "ApiId",
        "desc": "API唯一ID。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为 20，最大值为 100。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为 0。"
      }
    ],
    "desc": "本接口（DescribeApiEnvironmentStrategy）用于展示API绑定的限流策略。"
  },
  "UnBindSubDomain": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "服务唯一 ID。"
      },
      {
        "name": "SubDomain",
        "desc": "待解绑的自定义的域名。"
      }
    ],
    "desc": "本接口（UnBindSubDomain）用于解绑自定义域名。\n用户使用 API 网关绑定了自定义域名到服务中后，若想要解绑此自定义域名，可使用此接口。"
  },
  "DescribeServiceEnvironmentStrategy": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "服务唯一ID。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为 20，最大值为 100。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为 0。"
      }
    ],
    "desc": "本接口（DescribeServiceEnvironmentStrategy）用于展示服务限流策略。"
  },
  "DescribeServicesStatus": {
    "params": [
      {
        "name": "Limit",
        "desc": "返回数量，默认为 20，最大值为 100。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为 0。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件。支持ServiceId、ServiceName、NotUsagePlanId、Environment、IpVersion。"
      }
    ],
    "desc": "本接口（DescribeServicesStatus）用于搜索查询某一个服务或多个服务的列表，并返回服务相关的域名、时间等信息。"
  },
  "DeleteServiceSubDomainMapping": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "服务唯一 ID。"
      },
      {
        "name": "SubDomain",
        "desc": "服务绑定的自定义域名。"
      },
      {
        "name": "Environment",
        "desc": "待删除映射的环境名称，当前支持三个环境，test（测试环境）、prepub（预发布环境）和 release（发布环境）。"
      }
    ],
    "desc": "本接口（DeleteServiceSubDomainMapping）用于删除服务中某个环境的自定义域名映射。\n当用户使用自定义域名，并使用了自定义映射时，可使用此接口。但需注意，若删除了所有环境的映射时，调用此 API 均会返回失败。"
  },
  "DescribeApiKey": {
    "params": [
      {
        "name": "AccessKeyId",
        "desc": "API 密钥 ID。"
      }
    ],
    "desc": "本接口（DescribeApiKey）用于查询密钥详情。\n用户在创建密钥后，可用此接口查询一个 API 密钥的详情，该接口会显示密钥 Key。"
  },
  "DescribeUsagePlan": {
    "params": [
      {
        "name": "UsagePlanId",
        "desc": "待查询的使用计划唯一 ID。"
      }
    ],
    "desc": "本接口（DescribeUsagePlan）用于查询一个使用计划的详细信息，包括名称、QPS、创建时间绑定的环境等。"
  },
  "DescribeApi": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "API 所在的服务唯一 ID。"
      },
      {
        "name": "ApiId",
        "desc": "API 接口唯一 ID。"
      }
    ],
    "desc": "本接口（DescribeApi）用于查询用户部署于 API 网关的 API 接口的详细信息。​"
  },
  "BindSubDomain": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "服务唯一 ID。"
      },
      {
        "name": "SubDomain",
        "desc": "待绑定的自定义的域名。"
      },
      {
        "name": "Protocol",
        "desc": "服务支持协议，可选值为http、https、http&https。"
      },
      {
        "name": "NetType",
        "desc": "网络类型，可选值为OUTER、INNER。"
      },
      {
        "name": "IsDefaultMapping",
        "desc": "是否使用默认路径映射，默认为 true。为 false 时，表示自定义路径映射，此时 PathMappingSet 必填。"
      },
      {
        "name": "NetSubDomain",
        "desc": "默认域名。"
      },
      {
        "name": "CertificateId",
        "desc": "待绑定自定义域名的证书唯一 ID。针对Protocol 为https或http&https可以选择上传。"
      },
      {
        "name": "PathMappingSet",
        "desc": "自定义域名路径映射，最多输入三个Environment，并且只能分别取值“test”、 ”prepub“、”release“。"
      }
    ],
    "desc": "本接口（BindSubDomain）用于绑定自定义域名到服务。\nAPI 网关中每个服务都会提供一个默认的域名供用户调用，但当用户想使用自己的已有域名时，也可以将自定义域名绑定到此服务，在做好备案、与默认域名的 CNAME 后，可直接调用自定义域名。"
  },
  "DeleteIPStrategy": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "待删除的IP策略所属的服务唯一ID。"
      },
      {
        "name": "StrategyId",
        "desc": "待删除的IP策略唯一ID。"
      }
    ],
    "desc": "本接口（DeleteIPStrategy）用于删除服务IP策略。"
  },
  "GenerateApiDocument": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "待创建文档的服务唯一 ID。"
      },
      {
        "name": "GenEnvironment",
        "desc": "待创建 SDK 的服务所在环境。"
      },
      {
        "name": "GenLanguage",
        "desc": "待创建 SDK 的语言。当前只支持 Python 和 JavaScript。"
      }
    ],
    "desc": "本接口（GenerateApiDocument）用于自动生成 API 文档和 SDK，一个服务的一个环境生成一份文档和 SDK。"
  },
  "BindSecretIds": {
    "params": [
      {
        "name": "UsagePlanId",
        "desc": "待绑定的使用计划唯一 ID。"
      },
      {
        "name": "AccessKeyIds",
        "desc": "待绑定的密钥 ID 数组。"
      }
    ],
    "desc": "本接口（BindSecretIds）用于为使用计划绑定密钥。\n将密钥绑定到某个使用计划，并将此使用计划绑定到某个服务发布的环境上，调用者方可使用此密钥调用这个服务中的 API，可使用本接口为使用计划绑定密钥。"
  },
  "CreateApi": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "API 所在的服务唯一 ID。"
      },
      {
        "name": "ServiceType",
        "desc": "API 的后端服务类型。支持HTTP、MOCK、TSF、CLB、SCF、WEBSOCKET、TARGET（内测）。"
      },
      {
        "name": "ServiceTimeout",
        "desc": "API 的后端服务超时时间，单位是秒。"
      },
      {
        "name": "Protocol",
        "desc": "API 的前端请求类型，如 HTTP 或 HTTPS 或者 HTTP 和 HTTPS。"
      },
      {
        "name": "RequestConfig",
        "desc": "请求的前端配置。"
      },
      {
        "name": "ApiName",
        "desc": "用户自定义的 API 名称。"
      },
      {
        "name": "ApiDesc",
        "desc": "用户自定义的 API 接口描述。"
      },
      {
        "name": "ApiType",
        "desc": "API 类型，支持NORMAL（普通API）和TSF（微服务API），默认为NORMAL。"
      },
      {
        "name": "AuthType",
        "desc": "API 鉴权类型。支持SECRET（密钥对鉴权）、NONE（免鉴权）、OAUTH。默认为NONE。"
      },
      {
        "name": "EnableCORS",
        "desc": "是否开启跨域。"
      },
      {
        "name": "ConstantParameters",
        "desc": "常量参数。"
      },
      {
        "name": "RequestParameters",
        "desc": "前端请求参数。"
      },
      {
        "name": "ApiBusinessType",
        "desc": "当AuthType 为 OAUTH时，该字段有效， NORMAL：业务api OAUTH：授权API。"
      },
      {
        "name": "ServiceMockReturnMessage",
        "desc": "API 的后端 Mock 返回信息。如果 ServiceType 是 Mock，则此参数必传。"
      },
      {
        "name": "MicroServices",
        "desc": "API绑定微服务服务列表。"
      },
      {
        "name": "ServiceTsfLoadBalanceConf",
        "desc": "微服务的负载均衡配置。"
      },
      {
        "name": "ServiceTsfHealthCheckConf",
        "desc": "微服务的健康检查配置。"
      },
      {
        "name": "TargetServices",
        "desc": "target类型后端资源信息。（内测阶段）"
      },
      {
        "name": "TargetServicesLoadBalanceConf",
        "desc": "target类型负载均衡配置。（内测阶段）"
      },
      {
        "name": "TargetServicesHealthCheckConf",
        "desc": "target健康检查配置。（内测阶段）"
      },
      {
        "name": "ServiceScfFunctionName",
        "desc": "scf 函数名称。当后端类型是SCF时生效。"
      },
      {
        "name": "ServiceWebsocketRegisterFunctionName",
        "desc": "scf websocket注册函数。当前端类型是WEBSOCKET且后端类型是SCF时生效。"
      },
      {
        "name": "ServiceWebsocketCleanupFunctionName",
        "desc": "scf websocket清理函数。当前端类型是WEBSOCKET且后端类型是SCF时生效。"
      },
      {
        "name": "ServiceWebsocketTransportFunctionName",
        "desc": "scf websocket传输函数。当前端类型是WEBSOCKET且后端类型是SCF时生效。"
      },
      {
        "name": "ServiceScfFunctionNamespace",
        "desc": "scf 函数命名空间。当后端类型是SCF时生效。"
      },
      {
        "name": "ServiceScfFunctionQualifier",
        "desc": "scf函数版本。当后端类型是SCF时生效。"
      },
      {
        "name": "ServiceWebsocketRegisterFunctionNamespace",
        "desc": "scf websocket注册函数命名空间。当前端类型是WEBSOCKET且后端类型是SCF时生效。"
      },
      {
        "name": "ServiceWebsocketRegisterFunctionQualifier",
        "desc": "scf websocket传输函数版本。当前端类型是WEBSOCKET且后端类型是SCF时生效。"
      },
      {
        "name": "ServiceWebsocketTransportFunctionNamespace",
        "desc": "scf websocket传输函数命名空间。当前端类型是WEBSOCKET且后端类型是SCF时生效。"
      },
      {
        "name": "ServiceWebsocketTransportFunctionQualifier",
        "desc": "scf websocket传输函数版本。当前端类型是WEBSOCKET且后端类型是SCF时生效。"
      },
      {
        "name": "ServiceWebsocketCleanupFunctionNamespace",
        "desc": "scf websocket清理函数命名空间。当前端类型是WEBSOCKET且后端类型是SCF时生效。"
      },
      {
        "name": "ServiceWebsocketCleanupFunctionQualifier",
        "desc": "scf websocket清理函数版本。当前端类型是WEBSOCKET且后端类型是SCF时生效。"
      },
      {
        "name": "ServiceScfIsIntegratedResponse",
        "desc": "是否开启响应集成。当后端类型是SCF时生效。"
      },
      {
        "name": "IsDebugAfterCharge",
        "desc": "开始调试后计费。（云市场预留字段）"
      },
      {
        "name": "IsDeleteResponseErrorCodes",
        "desc": "是否删除自定义响应配置错误码，如果不传或者传 False，不删除，当传 True 时，则删除此 API 所有自定义响应配置错误码。"
      },
      {
        "name": "ResponseType",
        "desc": "返回类型。"
      },
      {
        "name": "ResponseSuccessExample",
        "desc": "自定义响应配置成功响应示例。"
      },
      {
        "name": "ResponseFailExample",
        "desc": "自定义响应配置失败响应示例。"
      },
      {
        "name": "ServiceConfig",
        "desc": "API 的后端服务配置。"
      },
      {
        "name": "AuthRelationApiId",
        "desc": "关联的授权API 唯一 ID，当AuthType为OAUTH且ApiBusinessType为NORMAL时生效。标示业务API绑定的oauth2.0授权API唯一ID。"
      },
      {
        "name": "ServiceParameters",
        "desc": "API的后端服务参数。"
      },
      {
        "name": "OauthConfig",
        "desc": "oauth配置。当AuthType是OAUTH时生效。"
      },
      {
        "name": "ResponseErrorCodes",
        "desc": "用户自定义错误码配置。"
      },
      {
        "name": "TargetNamespaceId",
        "desc": "tsf serverless 命名空间ID。（内测中）"
      },
      {
        "name": "UserType",
        "desc": "用户类型。"
      }
    ],
    "desc": "本接口（CreateApi）用于创建 API 接口，创建 API 前，用户需要先创建服务，每个 API 都有自己归属的服务。"
  },
  "DescribeServiceSubDomainMappings": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "服务唯一 ID。"
      },
      {
        "name": "SubDomain",
        "desc": "服务绑定的自定义域名。"
      }
    ],
    "desc": "本接口（DescribeServiceSubDomainMappings）用于查询自定义域名的路径映射。\nAPI 网关可绑定自定义域名到服务，并且可以对自定义域名的路径进行映射，可自定义不同的路径映射到服务中的三个环境，本接口用于查询绑定服务的自定义域名的路径映射列表。"
  }
}