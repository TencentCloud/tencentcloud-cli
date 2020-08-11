# -*- coding: utf-8 -*-
DESC = "cvm-2017-03-12"
INFO = {
  "CreateImage": {
    "params": [
      {
        "name": "ImageName",
        "desc": "镜像名称"
      },
      {
        "name": "InstanceId",
        "desc": "需要制作镜像的实例ID。"
      },
      {
        "name": "ImageDescription",
        "desc": "镜像描述"
      },
      {
        "name": "ForcePoweroff",
        "desc": "是否执行强制关机以制作镜像。\n取值范围：<br><li>TRUE：表示关机之后制作镜像<br><li>FALSE：表示开机状态制作镜像<br><br>默认取值：FALSE。<br><br>开机状态制作镜像，可能导致部分数据未备份，影响数据安全。"
      },
      {
        "name": "Sysprep",
        "desc": "创建Windows镜像时是否启用Sysprep"
      },
      {
        "name": "DataDiskIds",
        "desc": "基于实例创建整机镜像时，指定包含在镜像里的数据盘Id"
      },
      {
        "name": "SnapshotIds",
        "desc": "基于快照创建镜像，指定快照ID，必须包含一个系统盘快照。不可与InstanceId同时传入。"
      },
      {
        "name": "DryRun",
        "desc": "检测本次请求的是否成功，但不会对操作的资源产生任何影响"
      }
    ],
    "desc": "本接口(CreateImage)用于将实例的系统盘制作为新镜像，创建后的镜像可以用于创建实例。"
  },
  "DescribeInstancesStatus": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "按照一个或者多个实例ID查询。实例ID形如：`ins-11112222`。此参数的具体格式可参考API[简介](https://cloud.tencent.com/document/api/213/15688)的`ids.N`一节）。每次请求的实例的上限为100。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。"
      }
    ],
    "desc": "本接口 (DescribeInstancesStatus) 用于查询一个或多个实例的状态。\n\n* 可以根据实例`ID`来查询实例的状态。\n* 如果参数为空，返回当前用户一定数量（Limit所指定的数量，默认为20）的实例状态。"
  },
  "ModifyImageSharePermission": {
    "params": [
      {
        "name": "ImageId",
        "desc": "镜像ID，形如`img-gvbnzy6f`。镜像Id可以通过如下方式获取：<br><li>通过[DescribeImages](https://cloud.tencent.com/document/api/213/15715)接口返回的`ImageId`获取。<br><li>通过[镜像控制台](https://console.cloud.tencent.com/cvm/image)获取。 <br>镜像ID必须指定为状态为`NORMAL`的镜像。镜像状态请参考[镜像数据表](https://cloud.tencent.com/document/product/213/15753#Image)。"
      },
      {
        "name": "AccountIds",
        "desc": "接收分享镜像的账号Id列表，array型参数的格式可以参考[API简介](/document/api/213/568)。帐号ID不同于QQ号，查询用户帐号ID请查看[帐号信息](https://console.cloud.tencent.com/developer)中的帐号ID栏。"
      },
      {
        "name": "Permission",
        "desc": "操作，包括 `SHARE`，`CANCEL`。其中`SHARE`代表分享操作，`CANCEL`代表取消分享操作。"
      }
    ],
    "desc": "本接口（ModifyImageSharePermission）用于修改镜像分享信息。\n\n* 分享镜像后，被分享账户可以通过该镜像创建实例。\n* 每个自定义镜像最多可共享给50个账户。\n* 分享镜像无法更改名称，描述，仅可用于创建实例。\n* 只支持分享到对方账户相同地域。\n"
  },
  "InquiryPriceRunInstances": {
    "params": [
      {
        "name": "Placement",
        "desc": "实例所在的位置。通过该参数可以指定实例所属可用区，所属项目等属性。"
      },
      {
        "name": "ImageId",
        "desc": "指定有效的[镜像](https://cloud.tencent.com/document/product/213/4940)ID，格式形如`img-xxx`。镜像类型分为四种：<br/><li>公共镜像</li><li>自定义镜像</li><li>共享镜像</li><li>服务市场镜像</li><br/>可通过以下方式获取可用的镜像ID：<br/><li>`公共镜像`、`自定义镜像`、`共享镜像`的镜像ID可通过登录[控制台](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE)查询；`服务镜像市场`的镜像ID可通过[云市场](https://market.cloud.tencent.com/list)查询。</li><li>通过调用接口 [DescribeImages](https://cloud.tencent.com/document/api/213/15715) ，取返回信息中的`ImageId`字段。</li>"
      },
      {
        "name": "InstanceChargeType",
        "desc": "实例[计费类型](https://cloud.tencent.com/document/product/213/2180)。<br><li>PREPAID：预付费，即包年包月<br><li>POSTPAID_BY_HOUR：按小时后付费<br><li>SPOTPAID：竞价付费<br>默认值：POSTPAID_BY_HOUR。"
      },
      {
        "name": "InstanceChargePrepaid",
        "desc": "预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。"
      },
      {
        "name": "InstanceType",
        "desc": "实例机型。不同实例机型指定了不同的资源规格，具体取值可通过调用接口[DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749)来获得最新的规格表或参见[实例规格](https://cloud.tencent.com/document/product/213/11518)描述。若不指定该参数，则默认机型为S1.SMALL1。"
      },
      {
        "name": "SystemDisk",
        "desc": "实例系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。"
      },
      {
        "name": "DataDisks",
        "desc": "实例数据盘配置信息。若不指定该参数，则默认不购买数据盘。支持购买的时候指定21块数据盘，其中最多包含1块LOCAL_BASIC数据盘或者LOCAL_SSD数据盘，最多包含20块CLOUD_BASIC数据盘、CLOUD_PREMIUM数据盘或者CLOUD_SSD数据盘。"
      },
      {
        "name": "VirtualPrivateCloud",
        "desc": "私有网络相关信息配置。通过该参数可以指定私有网络的ID，子网ID等信息。若不指定该参数，则默认使用基础网络。若在此参数中指定了私有网络IP，那么InstanceCount参数只能为1。"
      },
      {
        "name": "InternetAccessible",
        "desc": "公网带宽相关信息设置。若不指定该参数，则默认公网带宽为0Mbps。"
      },
      {
        "name": "InstanceCount",
        "desc": "购买实例数量。取值范围：[1，100]。默认取值：1。指定购买实例的数量不能超过用户所能购买的剩余配额数量，具体配额相关限制详见[CVM实例购买限制](https://cloud.tencent.com/document/product/213/2664)。"
      },
      {
        "name": "InstanceName",
        "desc": "实例显示名称。<br><li>不指定实例显示名称则默认显示‘未命名’。</li><li>购买多台实例，如果指定模式串`{R:x}`，表示生成数字`[x, x+n-1]`，其中`n`表示购买实例的数量，例如`server_{R:3}`，购买1台时，实例显示名称为`server_3`；购买2台时，实例显示名称分别为`server_3`，`server_4`。支持指定多个模式串`{R:x}`。</li><li>购买多台实例，如果不指定模式串，则在实例显示名称添加后缀`1、2...n`，其中`n`表示购买实例的数量，例如`server_`，购买2台时，实例显示名称分别为`server_1`，`server_2`。</li><li>最多支持60个字符（包含模式串）。"
      },
      {
        "name": "LoginSettings",
        "desc": "实例登录设置。通过该参数可以设置实例的登录方式密码、密钥或保持镜像的原始登录设置。默认情况下会随机生成密码，并以站内信方式知会到用户。"
      },
      {
        "name": "SecurityGroupIds",
        "desc": "实例所属安全组。该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的sgId字段来获取。若不指定该参数，则默认不绑定安全组。"
      },
      {
        "name": "EnhancedService",
        "desc": "增强服务。通过该参数可以指定是否开启云安全、云监控等服务。若不指定该参数，则默认开启云监控、云安全服务。"
      },
      {
        "name": "ClientToken",
        "desc": "用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。<br>更多详细信息请参阅：如何保证幂等性。"
      },
      {
        "name": "HostName",
        "desc": "云服务器的主机名。<br><li>点号（.）和短横线（-）不能作为 HostName 的首尾字符，不能连续使用。<br><li>Windows 实例：名字符长度为[2, 15]，允许字母（不限制大小写）、数字和短横线（-）组成，不支持点号（.），不能全是数字。<br><li>其他类型（Linux 等）实例：字符长度为[2, 30]，允许支持多个点号，点之间为一段，每段允许字母（不限制大小写）、数字和短横线（-）组成。"
      },
      {
        "name": "TagSpecification",
        "desc": "标签描述列表。通过指定该参数可以同时绑定标签到相应的资源实例，当前仅支持绑定标签到云服务器实例。"
      },
      {
        "name": "InstanceMarketOptions",
        "desc": "实例的市场相关选项，如竞价实例相关参数"
      },
      {
        "name": "HpcClusterId",
        "desc": "高性能计算集群ID。"
      }
    ],
    "desc": "本接口(InquiryPriceRunInstances)用于创建实例询价。本接口仅允许针对购买限制范围内的实例配置进行询价, 详见：[创建实例](https://cloud.tencent.com/document/api/213/15730)。"
  },
  "DescribeImageSharePermission": {
    "params": [
      {
        "name": "ImageId",
        "desc": "需要共享的镜像Id"
      }
    ],
    "desc": "本接口（DescribeImageSharePermission）用于查询镜像分享信息。"
  },
  "ImportImage": {
    "params": [
      {
        "name": "Architecture",
        "desc": "导入镜像的操作系统架构，`x86_64` 或 `i386`"
      },
      {
        "name": "OsType",
        "desc": "导入镜像的操作系统类型，通过`DescribeImportImageOs`获取"
      },
      {
        "name": "OsVersion",
        "desc": "导入镜像的操作系统版本，通过`DescribeImportImageOs`获取"
      },
      {
        "name": "ImageUrl",
        "desc": "导入镜像存放的cos地址"
      },
      {
        "name": "ImageName",
        "desc": "镜像名称"
      },
      {
        "name": "ImageDescription",
        "desc": "镜像描述"
      },
      {
        "name": "DryRun",
        "desc": "只检查参数，不执行任务"
      },
      {
        "name": "Force",
        "desc": "是否强制导入，参考[强制导入镜像](https://cloud.tencent.com/document/product/213/12849)"
      }
    ],
    "desc": "本接口(ImportImage)用于导入镜像，导入后的镜像可用于创建实例。 "
  },
  "ModifyKeyPairAttribute": {
    "params": [
      {
        "name": "KeyId",
        "desc": "密钥对ID，密钥对ID形如：`skey-xxxxxxxx`。<br><br>可以通过以下方式获取可用的密钥 ID：<br><li>通过登录[控制台](https://console.cloud.tencent.com/cvm/sshkey)查询密钥 ID。<br><li>通过调用接口 [DescribeKeyPairs](https://cloud.tencent.com/document/api/213/9403) ，取返回信息中的 `KeyId` 获取密钥对 ID。"
      },
      {
        "name": "KeyName",
        "desc": "修改后的密钥对名称，可由数字，字母和下划线组成，长度不超过25个字符。"
      },
      {
        "name": "Description",
        "desc": "修改后的密钥对描述信息。可任意命名，但不得超过60个字符。"
      }
    ],
    "desc": "本接口 (ModifyKeyPairAttribute) 用于修改密钥对属性。\n\n* 修改密钥对ID所指定的密钥对的名称和描述信息。\n* 密钥对名称不能和已经存在的密钥对的名称重复。\n* 密钥对ID是密钥对的唯一标识，不可修改。"
  },
  "InquiryPriceRenewInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "一个或多个待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728)接口返回值中的`InstanceId`获取。每次请求批量实例的上限为100。"
      },
      {
        "name": "InstanceChargePrepaid",
        "desc": "预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的续费时长、是否设置自动续费等属性。"
      },
      {
        "name": "DryRun",
        "desc": "试运行，测试使用，不执行具体逻辑。取值范围：<br><li>TRUE：跳过执行逻辑<br><li>FALSE：执行逻辑<br><br>默认取值：FALSE。"
      },
      {
        "name": "RenewPortableDataDisk",
        "desc": "是否续费弹性数据盘。取值范围：<br><li>TRUE：表示续费包年包月实例同时续费其挂载的弹性数据盘<br><li>FALSE：表示续费包年包月实例同时不再续费其挂载的弹性数据盘<br><br>默认取值：TRUE。"
      }
    ],
    "desc": "本接口 (InquiryPriceRenewInstances) 用于续费包年包月实例询价。\n\n* 只支持查询包年包月实例的续费价格。"
  },
  "DescribeImages": {
    "params": [
      {
        "name": "ImageIds",
        "desc": "镜像ID列表 。镜像ID如：`img-gvbnzy6f`。array型参数的格式可以参考[API简介](https://cloud.tencent.com/document/api/213/15688)。镜像ID可以通过如下方式获取：<br><li>通过[DescribeImages](https://cloud.tencent.com/document/api/213/15715)接口返回的`ImageId`获取。<br><li>通过[镜像控制台](https://console.cloud.tencent.com/cvm/image)获取。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，每次请求的`Filters`的上限为0，`Filters.Values`的上限为5。参数不可以同时指定`ImageIds`和`Filters`。详细的过滤条件如下：\n<li> image-id - String - 是否必填： 否 - （过滤条件）按照镜像ID进行过滤</li>\n<li> image-type - String - 是否必填： 否 - （过滤条件）按照镜像类型进行过滤。取值范围：\n    PRIVATE_IMAGE: 私有镜像 (本账户创建的镜像) \n    PUBLIC_IMAGE: 公共镜像 (腾讯云官方镜像)\n   SHARED_IMAGE: 共享镜像(其他账户共享给本账户的镜像) 。</li>"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。关于Offset详见[API简介](/document/api/213/568#.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0.E4.B8.8E.E8.BF.94.E5.9B.9E.E5.8F.82.E6.95.B0.E9.87.8A.E4.B9.89)。"
      },
      {
        "name": "Limit",
        "desc": "数量限制，默认为20，最大值为100。关于Limit详见[API简介](/document/api/213/568#.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0.E4.B8.8E.E8.BF.94.E5.9B.9E.E5.8F.82.E6.95.B0.E9.87.8A.E4.B9.89)。"
      },
      {
        "name": "InstanceType",
        "desc": "实例类型，如 `S1.SMALL1`"
      }
    ],
    "desc": "本接口(DescribeImages) 用于查看镜像列表。\n\n* 可以通过指定镜像ID来查询指定镜像的详细信息，或通过设定过滤器来查询满足过滤条件的镜像的详细信息。\n* 指定偏移(Offset)和限制(Limit)来选择结果中的一部分，默认返回满足条件的前20个镜像信息。"
  },
  "ModifyInstancesAttribute": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "一个或多个待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728) API返回值中的`InstanceId`获取。每次请求允许操作的实例数量上限是100。"
      },
      {
        "name": "InstanceName",
        "desc": "实例名称。可任意命名，但不得超过60个字符。"
      },
      {
        "name": "SecurityGroups",
        "desc": "指定实例的安全组Id列表，子机将重新关联指定列表的安全组，原本关联的安全组会被解绑。"
      }
    ],
    "desc": "本接口 (ModifyInstancesAttribute) 用于修改实例的属性（目前只支持修改实例的名称和关联的安全组）。\n\n* “实例名称”仅为方便用户自己管理之用，腾讯云并不以此名称作为提交工单或是进行实例管理操作的依据。\n* 支持批量操作。每次请求批量实例的上限为100。\n* 修改关联安全组时，子机原来关联的安全组会被解绑。\n* 实例操作结果可以通过调用 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728#.E7.A4.BA.E4.BE.8B3-.E6.9F.A5.E8.AF.A2.E5.AE.9E.E4.BE.8B.E7.9A.84.E6.9C.80.E6.96.B0.E6.93.8D.E4.BD.9C.E6.83.85.E5.86.B5) 接口查询，如果实例的最新操作状态(LatestOperationState)为“SUCCESS”，则代表操作成功。"
  },
  "DescribeRegions": {
    "params": [],
    "desc": "本接口(DescribeRegions)用于查询地域信息。"
  },
  "InquiryPriceResetInstancesInternetMaxBandwidth": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "一个或多个待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728)接口返回值中的`InstanceId`获取。每次请求批量实例的上限为100。当调整 `BANDWIDTH_PREPAID` 和 `BANDWIDTH_POSTPAID_BY_HOUR` 计费方式的带宽时，只支持一个实例。"
      },
      {
        "name": "InternetAccessible",
        "desc": "公网出带宽配置。不同机型带宽上限范围不一致，具体限制详见带宽限制对账表。暂时只支持`InternetMaxBandwidthOut`参数。"
      },
      {
        "name": "StartTime",
        "desc": "带宽生效的起始时间。格式：`YYYY-MM-DD`，例如：`2016-10-30`。起始时间不能早于当前时间。如果起始时间是今天则新设置的带宽立即生效。该参数只对包年包月带宽有效，其他模式带宽不支持该参数，否则接口会以相应错误码返回。"
      },
      {
        "name": "EndTime",
        "desc": "带宽生效的终止时间。格式：`YYYY-MM-DD`，例如：`2016-10-30`。新设置的带宽的有效期包含终止时间此日期。终止时间不能晚于包年包月实例的到期时间。实例的到期时间可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728)接口返回值中的`ExpiredTime`获取。该参数只对包年包月带宽有效，其他模式带宽不支持该参数，否则接口会以相应错误码返回。"
      }
    ],
    "desc": "本接口 (InquiryPriceResetInstancesInternetMaxBandwidth) 用于调整实例公网带宽上限询价。\n\n* 不同机型带宽上限范围不一致，具体限制详见[公网带宽上限](https://cloud.tencent.com/document/product/213/12523)。\n* 对于`BANDWIDTH_PREPAID`计费方式的带宽，目前不支持调小带宽，且需要输入参数`StartTime`和`EndTime`，指定调整后的带宽的生效时间段。在这种场景下会涉及扣费，请确保账户余额充足。可通过[`DescribeAccountBalance`](https://cloud.tencent.com/document/product/555/20253)接口查询账户余额。\n* 对于 `TRAFFIC_POSTPAID_BY_HOUR`、 `BANDWIDTH_POSTPAID_BY_HOUR` 和 `BANDWIDTH_PACKAGE` 计费方式的带宽，使用该接口调整带宽上限是实时生效的，可以在带宽允许的范围内调大或者调小带宽，不支持输入参数 `StartTime` 和 `EndTime` 。\n* 接口不支持调整`BANDWIDTH_POSTPAID_BY_MONTH`计费方式的带宽。\n* 接口不支持批量调整 `BANDWIDTH_PREPAID` 和 `BANDWIDTH_POSTPAID_BY_HOUR` 计费方式的带宽。\n* 接口不支持批量调整混合计费方式的带宽。例如不支持同时调整`TRAFFIC_POSTPAID_BY_HOUR`和`BANDWIDTH_PACKAGE`计费方式的带宽。"
  },
  "DeleteImages": {
    "params": [
      {
        "name": "ImageIds",
        "desc": "准备删除的镜像Id列表"
      }
    ],
    "desc": "本接口（DeleteImages）用于删除一个或多个镜像。\n\n* 当[镜像状态](https://cloud.tencent.com/document/product/213/15753#Image)为`创建中`和`使用中`时, 不允许删除。镜像状态可以通过[DescribeImages](https://cloud.tencent.com/document/api/213/9418)获取。\n* 每个地域最多只支持创建10个自定义镜像，删除镜像可以释放账户的配额。\n* 当镜像正在被其它账户分享时，不允许删除。"
  },
  "CreateKeyPair": {
    "params": [
      {
        "name": "KeyName",
        "desc": "密钥对名称，可由数字，字母和下划线组成，长度不超过25个字符。"
      },
      {
        "name": "ProjectId",
        "desc": "密钥对创建后所属的项目ID。\n可以通过以下方式获取项目ID：\n<li>通过项目列表查询项目ID。\n<li>通过调用接口DescribeProject，取返回信息中的`projectId `获取项目ID。"
      }
    ],
    "desc": "本接口 (CreateKeyPair) 用于创建一个 `OpenSSH RSA` 密钥对，可以用于登录 `Linux` 实例。\n\n* 开发者只需指定密钥对名称，即可由系统自动创建密钥对，并返回所生成的密钥对的 `ID` 及其公钥、私钥的内容。\n* 密钥对名称不能和已经存在的密钥对的名称重复。\n* 私钥的内容可以保存到文件中作为 `SSH` 的一种认证方式。\n* 腾讯云不会保存用户的私钥，请妥善保管。"
  },
  "DescribeInstanceFamilyConfigs": {
    "params": [],
    "desc": "本接口（DescribeInstanceFamilyConfigs）查询当前用户和地域所支持的机型族列表信息。"
  },
  "DeleteKeyPairs": {
    "params": [
      {
        "name": "KeyIds",
        "desc": "一个或多个待操作的密钥对ID。每次请求批量密钥对的上限为100。<br>可以通过以下方式获取可用的密钥ID：<br><li>通过登录[控制台](https://console.cloud.tencent.com/cvm/sshkey)查询密钥ID。<br><li>通过调用接口 [DescribeKeyPairs](https://cloud.tencent.com/document/api/213/15699) ，取返回信息中的 `KeyId` 获取密钥对ID。"
      }
    ],
    "desc": "本接口 (DeleteKeyPairs) 用于删除已在腾讯云托管的密钥对。\n\n* 可以同时删除多个密钥对。\n* 不能删除已被实例或镜像引用的密钥对，所以需要独立判断是否所有密钥对都被成功删除。"
  },
  "CreateDisasterRecoverGroup": {
    "params": [
      {
        "name": "Name",
        "desc": "分散置放群组名称，长度1-60个字符，支持中、英文。"
      },
      {
        "name": "Type",
        "desc": "分散置放群组类型，取值范围：<br><li>HOST：物理机<br><li>SW：交换机<br><li>RACK：机架"
      },
      {
        "name": "ClientToken",
        "desc": "用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。<br>更多详细信息请参阅：如何保证幂等性。"
      }
    ],
    "desc": "本接口 (CreateDisasterRecoverGroup)用于创建[分散置放群组](https://cloud.tencent.com/document/product/213/15486)。创建好的置放群组，可在[创建实例](https://cloud.tencent.com/document/api/213/15730)时指定。"
  },
  "DescribeInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "按照一个或者多个实例ID查询。实例ID形如：`ins-xxxxxxxx`。（此参数的具体格式可参考API[简介](https://cloud.tencent.com/document/api/213/15688)的`ids.N`一节）。每次请求的实例的上限为100。参数不支持同时指定`InstanceIds`和`Filters`。"
      },
      {
        "name": "Filters",
        "desc": "<li><strong>zone</strong></li>\n<p style=\"padding-left: 30px;\">按照【<strong>可用区</strong>】进行过滤。可用区形如：ap-guangzhou-1。</p><p style=\"padding-left: 30px;\">类型：String</p><p style=\"padding-left: 30px;\">必选：否</p><p style=\"padding-left: 30px;\">可选项：<a href=\"https://cloud.tencent.com/document/product/213/6091\">可用区列表</a></p>\n<li><strong>project-id</strong></li>\n<p style=\"padding-left: 30px;\">按照【<strong>项目ID</strong>】进行过滤，可通过调用[DescribeProject](https://cloud.tencent.com/document/api/378/4400)查询已创建的项目列表或登录[控制台](https://console.cloud.tencent.com/cvm/index)进行查看；也可以调用[AddProject](https://cloud.tencent.com/document/api/378/4398)创建新的项目。项目ID形如：1002189。</p><p style=\"padding-left: 30px;\">类型：Integer</p><p style=\"padding-left: 30px;\">必选：否</p>\n<li><strong>host-id</strong></li>\n<p style=\"padding-left: 30px;\">按照【<strong>[CDH](https://cloud.tencent.com/document/product/416) ID</strong>】进行过滤。[CDH](https://cloud.tencent.com/document/product/416) ID形如：host-xxxxxxxx。</p><p style=\"padding-left: 30px;\">类型：String</p><p style=\"padding-left: 30px;\">必选：否</p>\n<li><strong>vpc-id</strong></li>\n<p style=\"padding-left: 30px;\">按照【<strong>VPC ID</strong>】进行过滤。VPC ID形如：vpc-xxxxxxxx。</p><p style=\"padding-left: 30px;\">类型：String</p><p style=\"padding-left: 30px;\">必选：否</p>\n<li><strong>subnet-id</strong></li>\n<p style=\"padding-left: 30px;\">按照【<strong>子网ID</strong>】进行过滤。子网ID形如：subnet-xxxxxxxx。</p><p style=\"padding-left: 30px;\">类型：String</p><p style=\"padding-left: 30px;\">必选：否</p>\n<li><strong>instance-id</strong></li>\n<p style=\"padding-left: 30px;\">按照【<strong>实例ID</strong>】进行过滤。实例ID形如：ins-xxxxxxxx。</p><p style=\"padding-left: 30px;\">类型：String</p><p style=\"padding-left: 30px;\">必选：否</p>\n<li><strong>security-group-id</strong></li>\n<p style=\"padding-left: 30px;\">按照【<strong>安全组ID</strong>】进行过滤。安全组ID形如: sg-8jlk3f3r。</p><p style=\"padding-left: 30px;\">类型：String</p><p style=\"padding-left: 30px;\">必选：否</p>\n<li><strong>instance-name</strong></li>\n<p style=\"padding-left: 30px;\">按照【<strong>实例名称</strong>】进行过滤。</p><p style=\"padding-left: 30px;\">类型：String</p><p style=\"padding-left: 30px;\">必选：否</p>\n<li><strong>instance-charge-type</strong></li>\n<p style=\"padding-left: 30px;\">按照【<strong>实例计费模式</strong>】进行过滤。(PREPAID：表示预付费，即包年包月 | POSTPAID_BY_HOUR：表示后付费，即按量计费 | CDHPAID：表示[CDH](https://cloud.tencent.com/document/product/416)付费，即只对[CDH](https://cloud.tencent.com/document/product/416)计费，不对[CDH](https://cloud.tencent.com/document/product/416)上的实例计费。)</p><p style=\"padding-left: 30px;\">类型：String</p><p style=\"padding-left: 30px;\">必选：否</p>\n<li><strong>private-ip-address</strong></li>\n<p style=\"padding-left: 30px;\">按照【<strong>实例主网卡的内网IP</strong>】进行过滤。</p><p style=\"padding-left: 30px;\">类型：String</p><p style=\"padding-left: 30px;\">必选：否</p>\n<li><strong>public-ip-address</strong></li>\n<p style=\"padding-left: 30px;\">按照【<strong>实例主网卡的公网IP</strong>】进行过滤，包含实例创建时自动分配的IP和实例创建后手动绑定的弹性IP。</p><p style=\"padding-left: 30px;\">类型：String</p><p style=\"padding-left: 30px;\">必选：否</p>\n<li><strong>tag-key</strong></li>\n<p style=\"padding-left: 30px;\">按照【<strong>标签键</strong>】进行过滤。</p><p style=\"padding-left: 30px;\">类型：String</p><p style=\"padding-left: 30px;\">必选：否</p>\n<li><strong>tag-value</strong></li>\n<p style=\"padding-left: 30px;\">按照【<strong>标签值</strong>】进行过滤。</p><p style=\"padding-left: 30px;\">类型：String</p><p style=\"padding-left: 30px;\">必选：否</p>\n<li><strong>tag:tag-key</strong></li>\n<p style=\"padding-left: 30px;\">按照【<strong>标签键值对</strong>】进行过滤。tag-key使用具体的标签键进行替换。使用请参考示例2。</p><p style=\"padding-left: 30px;\">类型：String</p><p style=\"padding-left: 30px;\">必选：否</p>\n每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。参数不支持同时指定`InstanceIds`和`Filters`。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。"
      }
    ],
    "desc": "本接口 (DescribeInstances) 用于查询一个或多个实例的详细信息。\n\n* 可以根据实例`ID`、实例名称或者实例计费模式等信息来查询实例的详细信息。过滤信息详细请见过滤器`Filter`。\n* 如果参数为空，返回当前用户一定数量（`Limit`所指定的数量，默认为20）的实例。\n* 支持查询实例的最新操作（LatestOperation）以及最新操作状态(LatestOperationState)。"
  },
  "ImportKeyPair": {
    "params": [
      {
        "name": "KeyName",
        "desc": "密钥对名称，可由数字，字母和下划线组成，长度不超过25个字符。"
      },
      {
        "name": "ProjectId",
        "desc": "密钥对创建后所属的[项目](https://cloud.tencent.com/document/product/378/10861)ID。<br><br>可以通过以下方式获取项目ID：<br><li>通过[项目列表](https://console.cloud.tencent.com/project)查询项目ID。<br><li>通过调用接口 [DescribeProject](https://cloud.tencent.com/document/api/378/4400)，取返回信息中的 `projectId ` 获取项目ID。\n\n如果是默认项目，直接填0就可以。"
      },
      {
        "name": "PublicKey",
        "desc": "密钥对的公钥内容，`OpenSSH RSA` 格式。"
      }
    ],
    "desc": "本接口 (ImportKeyPair) 用于导入密钥对。\n\n* 本接口的功能是将密钥对导入到用户账户，并不会自动绑定到实例。如需绑定可以使用[AssociasteInstancesKeyPair](https://cloud.tencent.com/document/api/213/9404)接口。\n* 需指定密钥对名称以及该密钥对的公钥文本。\n* 如果用户只有私钥，可以通过 `SSL` 工具将私钥转换成公钥后再导入。"
  },
  "DescribeInstanceInternetBandwidthConfigs": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728)接口返回值中的`InstanceId`获取。"
      }
    ],
    "desc": "本接口 (DescribeInstanceInternetBandwidthConfigs) 用于查询实例带宽配置。\n\n* 只支持查询`BANDWIDTH_PREPAID`（ 预付费按带宽结算 ）计费模式的带宽配置。\n* 接口返回实例的所有带宽配置信息（包含历史的带宽配置信息）。"
  },
  "AssociateInstancesKeyPairs": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "一个或多个待操作的实例ID，每次请求批量实例的上限为100。<br>可以通过以下方式获取可用的实例ID：<br><li>通过登录[控制台](https://console.cloud.tencent.com/cvm/index)查询实例ID。<br><li>通过调用接口 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) ，取返回信息中的`InstanceId`获取实例ID。"
      },
      {
        "name": "KeyIds",
        "desc": "一个或多个待操作的密钥对ID，每次请求批量密钥对的上限为100。密钥对ID形如：`skey-3glfot13`。<br>可以通过以下方式获取可用的密钥ID：<br><li>通过登录[控制台](https://console.cloud.tencent.com/cvm/sshkey)查询密钥ID。<br><li>通过调用接口 [DescribeKeyPairs](https://cloud.tencent.com/document/api/213/15699) ，取返回信息中的`KeyId`获取密钥对ID。"
      },
      {
        "name": "ForceStop",
        "desc": "是否对运行中的实例选择强制关机。建议对运行中的实例先手动关机，然后再绑定密钥。取值范围：<br><li>TRUE：表示在正常关机失败后进行强制关机。<br><li>FALSE：表示在正常关机失败后不进行强制关机。<br>默认取值：FALSE。"
      }
    ],
    "desc": "本接口 (AssociateInstancesKeyPairs) 用于将密钥绑定到实例上。\n\n* 将密钥的公钥写入到实例的`SSH`配置当中，用户就可以通过该密钥的私钥来登录实例。\n* 如果实例原来绑定过密钥，那么原来的密钥将失效。\n* 如果实例原来是通过密码登录，绑定密钥后无法使用密码登录。\n* 支持批量操作。每次请求批量实例的上限为100。如果批量实例存在不允许操作的实例，操作会以特定错误码返回。"
  },
  "RunInstances": {
    "params": [
      {
        "name": "Placement",
        "desc": "实例所在的位置。通过该参数可以指定实例所属可用区，所属项目，所属宿主机（在专用宿主机上创建子机时指定）等属性。"
      },
      {
        "name": "ImageId",
        "desc": "指定有效的[镜像](https://cloud.tencent.com/document/product/213/4940)ID，格式形如`img-xxx`。镜像类型分为四种：<br/><li>公共镜像</li><li>自定义镜像</li><li>共享镜像</li><li>服务市场镜像</li><br/>可通过以下方式获取可用的镜像ID：<br/><li>`公共镜像`、`自定义镜像`、`共享镜像`的镜像ID可通过登录[控制台](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE)查询；`服务镜像市场`的镜像ID可通过[云市场](https://market.cloud.tencent.com/list)查询。</li><li>通过调用接口 [DescribeImages](https://cloud.tencent.com/document/api/213/15715) ，传入InstanceType获取当前机型支持的镜像列表，取返回信息中的`ImageId`字段。</li>"
      },
      {
        "name": "InstanceChargeType",
        "desc": "实例[计费类型](https://cloud.tencent.com/document/product/213/2180)。<br><li>PREPAID：预付费，即包年包月<br><li>POSTPAID_BY_HOUR：按小时后付费<br><li>CDHPAID：独享子机（基于专用宿主机创建，宿主机部分的资源不收费）<br><li>SPOTPAID：竞价付费<br>默认值：POSTPAID_BY_HOUR。"
      },
      {
        "name": "InstanceChargePrepaid",
        "desc": "预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。"
      },
      {
        "name": "InstanceType",
        "desc": "实例机型。不同实例机型指定了不同的资源规格。\n<br><li>对于付费模式为PREPAID或POSTPAID\\_BY\\_HOUR的实例创建，具体取值可通过调用接口[DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749)来获得最新的规格表或参见[实例规格](https://cloud.tencent.com/document/product/213/11518)描述。若不指定该参数，则默认机型为S1.SMALL1。<br><li>对于付费模式为CDHPAID的实例创建，该参数以\"CDH_\"为前缀，根据CPU和内存配置生成，具体形式为：CDH_XCXG，例如对于创建CPU为1核，内存为1G大小的专用宿主机的实例，该参数应该为CDH_1C1G。"
      },
      {
        "name": "SystemDisk",
        "desc": "实例系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。"
      },
      {
        "name": "DataDisks",
        "desc": "实例数据盘配置信息。若不指定该参数，则默认不购买数据盘。支持购买的时候指定21块数据盘，其中最多包含1块LOCAL_BASIC数据盘或者LOCAL_SSD数据盘，最多包含20块CLOUD_BASIC数据盘、CLOUD_PREMIUM数据盘或者CLOUD_SSD数据盘。"
      },
      {
        "name": "VirtualPrivateCloud",
        "desc": "私有网络相关信息配置。通过该参数可以指定私有网络的ID，子网ID等信息。若不指定该参数，则默认使用基础网络。若在此参数中指定了私有网络IP，即表示每个实例的主网卡IP；同时，InstanceCount参数必须与私有网络IP的个数一致且不能大于20。"
      },
      {
        "name": "InternetAccessible",
        "desc": "公网带宽相关信息设置。若不指定该参数，则默认公网带宽为0Mbps。"
      },
      {
        "name": "InstanceCount",
        "desc": "购买实例数量。包年包月实例取值范围：[1，300]，按量计费实例取值范围：[1，100]。默认取值：1。指定购买实例的数量不能超过用户所能购买的剩余配额数量，具体配额相关限制详见[CVM实例购买限制](https://cloud.tencent.com/document/product/213/2664)。"
      },
      {
        "name": "InstanceName",
        "desc": "实例显示名称。<br><li>不指定实例显示名称则默认显示‘未命名’。</li><li>购买多台实例，如果指定模式串`{R:x}`，表示生成数字`[x, x+n-1]`，其中`n`表示购买实例的数量，例如`server_{R:3}`，购买1台时，实例显示名称为`server_3`；购买2台时，实例显示名称分别为`server_3`，`server_4`。支持指定多个模式串`{R:x}`。</li><li>购买多台实例，如果不指定模式串，则在实例显示名称添加后缀`1、2...n`，其中`n`表示购买实例的数量，例如`server_`，购买2台时，实例显示名称分别为`server_1`，`server_2`。</li><li>最多支持60个字符（包含模式串）。"
      },
      {
        "name": "LoginSettings",
        "desc": "实例登录设置。通过该参数可以设置实例的登录方式密码、密钥或保持镜像的原始登录设置。默认情况下会随机生成密码，并以站内信方式知会到用户。"
      },
      {
        "name": "SecurityGroupIds",
        "desc": "实例所属安全组。该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的sgId字段来获取。若不指定该参数，则绑定默认安全组。"
      },
      {
        "name": "EnhancedService",
        "desc": "增强服务。通过该参数可以指定是否开启云安全、云监控等服务。若不指定该参数，则默认公共镜像开启云监控、云安全服务；自定义镜像与镜像市场镜像默认不开启云监控，云安全服务，而使用镜像里保留的服务。"
      },
      {
        "name": "ClientToken",
        "desc": "用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。"
      },
      {
        "name": "HostName",
        "desc": "云服务器的主机名。<br><li>点号（.）和短横线（-）不能作为 HostName 的首尾字符，不能连续使用。<br><li>Windows 实例：名字符长度为[2, 15]，允许字母（不限制大小写）、数字和短横线（-）组成，不支持点号（.），不能全是数字。<br><li>其他类型（Linux 等）实例：字符长度为[2, 60]，允许支持多个点号，点之间为一段，每段允许字母（不限制大小写）、数字和短横线（-）组成。"
      },
      {
        "name": "ActionTimer",
        "desc": "定时任务。通过该参数可以为实例指定定时任务，目前仅支持定时销毁。"
      },
      {
        "name": "DisasterRecoverGroupIds",
        "desc": "置放群组id，仅支持指定一个。"
      },
      {
        "name": "TagSpecification",
        "desc": "标签描述列表。通过指定该参数可以同时绑定标签到相应的资源实例，当前仅支持绑定标签到云服务器实例。"
      },
      {
        "name": "InstanceMarketOptions",
        "desc": "实例的市场相关选项，如竞价实例相关参数，若指定实例的付费模式为竞价付费则该参数必传。"
      },
      {
        "name": "UserData",
        "desc": "提供给实例使用的用户数据，需要以 base64 方式编码，支持的最大数据大小为 16KB。关于获取此参数的详细介绍，请参阅[Windows](https://cloud.tencent.com/document/product/213/17526)和[Linux](https://cloud.tencent.com/document/product/213/17525)启动时运行命令。"
      },
      {
        "name": "DryRun",
        "desc": "是否只预检此次请求。\ntrue：发送检查请求，不会创建实例。检查项包括是否填写了必需参数，请求格式，业务限制和云服务器库存。\n如果检查不通过，则返回对应错误码；\n如果检查通过，则返回RequestId.\nfalse（默认）：发送正常请求，通过检查后直接创建实例"
      },
      {
        "name": "HpcClusterId",
        "desc": "高性能计算集群ID。若创建的实例为高性能计算实例，需指定实例放置的集群，否则不可指定。"
      }
    ],
    "desc": "本接口 (RunInstances) 用于创建一个或多个指定配置的实例。\n\n* 实例创建成功后将自动开机启动，[实例状态](https://cloud.tencent.com/document/product/213/15753#InstanceStatus)变为“运行中”。\n* 预付费实例的购买会预先扣除本次实例购买所需金额，按小时后付费实例购买会预先冻结本次实例购买一小时内所需金额，在调用本接口前请确保账户余额充足。\n* 本接口允许购买的实例数量遵循[CVM实例购买限制](https://cloud.tencent.com/document/product/213/2664)，所创建的实例和官网入口创建的实例共用配额。\n* 本接口为异步接口，当创建实例请求下发成功后会返回一个实例`ID`列表和一个`RequestId`，此时创建实例操作并未立即完成。在此期间实例的状态将会处于“PENDING”，实例创建结果可以通过调用 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728)  接口查询，如果实例状态(InstanceState)由“PENDING”变为“RUNNING”，则代表实例创建成功，“LAUNCH_FAILED”代表实例创建失败。"
  },
  "DisassociateInstancesKeyPairs": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "一个或多个待操作的实例ID，每次请求批量实例的上限为100。<br><br>可以通过以下方式获取可用的实例ID：<br><li>通过登录[控制台](https://console.cloud.tencent.com/cvm/index)查询实例ID。<br><li>通过调用接口 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) ，取返回信息中的 `InstanceId` 获取实例ID。"
      },
      {
        "name": "KeyIds",
        "desc": "密钥对ID列表，每次请求批量密钥对的上限为100。密钥对ID形如：`skey-11112222`。<br><br>可以通过以下方式获取可用的密钥ID：<br><li>通过登录[控制台](https://console.cloud.tencent.com/cvm/sshkey)查询密钥ID。<br><li>通过调用接口 [DescribeKeyPairs](https://cloud.tencent.com/document/api/213/15699) ，取返回信息中的 `KeyId` 获取密钥对ID。"
      },
      {
        "name": "ForceStop",
        "desc": "是否对运行中的实例选择强制关机。建议对运行中的实例先手动关机，然后再解绑密钥。取值范围：<br><li>TRUE：表示在正常关机失败后进行强制关机。<br><li>FALSE：表示在正常关机失败后不进行强制关机。<br><br>默认取值：FALSE。"
      }
    ],
    "desc": "本接口 (DisassociateInstancesKeyPairs) 用于解除实例的密钥绑定关系。\n\n* 只支持[`STOPPED`](https://cloud.tencent.com/document/product/213/15753#InstanceStatus)状态的`Linux`操作系统的实例。\n* 解绑密钥后，实例可以通过原来设置的密码登录。\n* 如果原来没有设置密码，解绑后将无法使用 `SSH` 登录。可以调用 [ResetInstancesPassword](https://cloud.tencent.com/document/api/213/15736) 接口来设置登录密码。\n* 支持批量操作。每次请求批量实例的上限为100。如果批量实例存在不允许操作的实例，操作会以特定错误码返回。"
  },
  "InquiryPriceResizeInstanceDisks": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728)接口返回值中的`InstanceId`获取。"
      },
      {
        "name": "DataDisks",
        "desc": "待扩容的数据盘配置信息。只支持扩容非弹性数据盘（[`DescribeDisks`](https://cloud.tencent.com/document/api/362/16315)接口返回值中的`Portable`为`false`表示非弹性），且[数据盘类型](https://cloud.tencent.com/document/product/213/15753#DataDisk)为：`CLOUD_BASIC`、`CLOUD_PREMIUM`、`CLOUD_SSD`。数据盘容量单位：GB。最小扩容步长：10G。关于数据盘类型的选择请参考硬盘产品简介。可选数据盘类型受到实例类型`InstanceType`限制。另外允许扩容的最大容量也因数据盘类型的不同而有所差异。"
      },
      {
        "name": "ForceStop",
        "desc": "是否对运行中的实例选择强制关机。建议对运行中的实例先手动关机，然后再重置用户密码。取值范围：<br><li>TRUE：表示在正常关机失败后进行强制关机<br><li>FALSE：表示在正常关机失败后不进行强制关机<br><br>默认取值：FALSE。<br><br>强制关机的效果等同于关闭物理计算机的电源开关。强制关机可能会导致数据丢失或文件系统损坏，请仅在服务器不能正常关机时使用。"
      }
    ],
    "desc": "本接口 (InquiryPriceResizeInstanceDisks) 用于扩容实例的数据盘询价。\n\n* 目前只支持扩容非弹性数据盘（[`DescribeDisks`](https://cloud.tencent.com/document/api/362/16315)接口返回值中的`Portable`为`false`表示非弹性）询价，且[数据盘类型](https://cloud.tencent.com/document/product/213/15753#DataDisk)为：`CLOUD_BASIC`、`CLOUD_PREMIUM`、`CLOUD_SSD`。\n* 目前不支持[CDH](https://cloud.tencent.com/document/product/416)实例使用该接口扩容数据盘询价。* 仅支持包年包月实例随机器购买的数据盘。* 目前只支持扩容一块数据盘询价。"
  },
  "ModifyInstancesVpcAttribute": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "待操作的实例ID数组。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728)接口返回值中的`InstanceId`获取。"
      },
      {
        "name": "VirtualPrivateCloud",
        "desc": "私有网络相关信息配置，通过该参数指定私有网络的ID，子网ID，私有网络ip等信息。<br><li>当指定私有网络ID和子网ID（子网必须在实例所在的可用区）与指定实例所在私有网络不一致时，会将实例迁移至指定的私有网络的子网下。<br><li>可通过`PrivateIpAddresses`指定私有网络子网IP，若需指定则所有已指定的实例均需要指定子网IP，此时`InstanceIds`与`PrivateIpAddresses`一一对应。<br><li>不指定`PrivateIpAddresses`时随机分配私有网络子网IP。"
      },
      {
        "name": "ForceStop",
        "desc": "是否对运行中的实例选择强制关机。默认为TRUE。"
      },
      {
        "name": "ReserveHostName",
        "desc": "是否保留主机名。默认为FALSE。"
      }
    ],
    "desc": "本接口(ModifyInstancesVpcAttribute)用于修改实例vpc属性，如私有网络ip。\n* 此操作默认会关闭实例，完成后再启动。\n* 当指定私有网络ID和子网ID（子网必须在实例所在的可用区）与指定实例所在私有网络不一致时，会将实例迁移至指定的私有网络的子网下。执行此操作前请确保指定的实例上没有绑定[弹性网卡](https://cloud.tencent.com/document/product/576)和[负载均衡](https://cloud.tencent.com/document/product/214)。\n* 实例操作结果可以通过调用 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728#.E7.A4.BA.E4.BE.8B3-.E6.9F.A5.E8.AF.A2.E5.AE.9E.E4.BE.8B.E7.9A.84.E6.9C.80.E6.96.B0.E6.93.8D.E4.BD.9C.E6.83.85.E5.86.B5) 接口查询，如果实例的最新操作状态(LatestOperationState)为“SUCCESS”，则代表操作成功。"
  },
  "InquiryPriceResetInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID。可通过 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) API返回值中的`InstanceId`获取。"
      },
      {
        "name": "ImageId",
        "desc": "指定有效的[镜像](/document/product/213/4940)ID，格式形如`img-xxx`。镜像类型分为四种：<br/><li>公共镜像</li><li>自定义镜像</li><li>共享镜像</li><li>服务市场镜像</li><br/>可通过以下方式获取可用的镜像ID：<br/><li>`公共镜像`、`自定义镜像`、`共享镜像`的镜像ID可通过登录[控制台](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE)查询；`服务镜像市场`的镜像ID可通过[云市场](https://market.cloud.tencent.com/list)查询。</li><li>通过调用接口 [DescribeImages](https://cloud.tencent.com/document/api/213/15715) ，取返回信息中的`ImageId`字段。</li>"
      },
      {
        "name": "SystemDisk",
        "desc": "实例系统盘配置信息。系统盘为云盘的实例可以通过该参数指定重装后的系统盘大小来实现对系统盘的扩容操作，若不指定则默认系统盘大小保持不变。系统盘大小只支持扩容不支持缩容；重装只支持修改系统盘的大小，不能修改系统盘的类型。"
      },
      {
        "name": "LoginSettings",
        "desc": "实例登录设置。通过该参数可以设置实例的登录方式密码、密钥或保持镜像的原始登录设置。默认情况下会随机生成密码，并以站内信方式知会到用户。"
      },
      {
        "name": "EnhancedService",
        "desc": "增强服务。通过该参数可以指定是否开启云安全、云监控等服务。若不指定该参数，则默认开启云监控、云安全服务。"
      }
    ],
    "desc": "本接口 (InquiryPriceResetInstance) 用于重装实例询价。\n\n* 如果指定了`ImageId`参数，则使用指定的镜像进行重装询价；否则按照当前实例使用的镜像进行重装询价。\n* 目前只支持[系统盘类型](https://cloud.tencent.com/document/api/213/15753#SystemDisk)是`CLOUD_BASIC`、`CLOUD_PREMIUM`、`CLOUD_SSD`类型的实例使用该接口实现`Linux`和`Windows`操作系统切换的重装询价。\n* 目前不支持境外地域的实例使用该接口实现`Linux`和`Windows`操作系统切换的重装询价。"
  },
  "DescribeDisasterRecoverGroupQuota": {
    "params": [],
    "desc": "本接口 (DescribeDisasterRecoverGroupQuota)用于查询[分散置放群组](https://cloud.tencent.com/document/product/213/15486)配额。"
  },
  "ResetInstancesPassword": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "一个或多个待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728) API返回值中的`InstanceId`获取。每次请求允许操作的实例数量上限是100。"
      },
      {
        "name": "Password",
        "desc": "实例登录密码。不同操作系统类型密码复杂度限制不一样，具体如下：\nLinux实例密码必须8-30位，推荐使用12位以上密码，不能以“/”开头，至少包含以下字符中的三种不同字符，字符种类：<br><li>小写字母：[a-z]<br><li>大写字母：[A-Z]<br><li>数字：0-9<br><li>特殊字符： ()\\`~!@#$%^&\\*-+=\\_|{}[]:;'<>,.?/\nWindows实例密码必须12~30位，不能以“/”开头且不包括用户名，至少包含以下字符中的三种不同字符<br><li>小写字母：[a-z]<br><li>大写字母：[A-Z]<br><li>数字： 0-9<br><li>特殊字符：()\\`~!@#$%^&\\*-+=\\_|{}[]:;' <>,.?/<br><li>如果实例即包含`Linux`实例又包含`Windows`实例，则密码复杂度限制按照`Windows`实例的限制。"
      },
      {
        "name": "UserName",
        "desc": "待重置密码的实例操作系统的用户名。不得超过64个字符。"
      },
      {
        "name": "ForceStop",
        "desc": "是否对运行中的实例选择强制关机。建议对运行中的实例先手动关机，然后再重置用户密码。取值范围：<br><li>TRUE：表示在正常关机失败后进行强制关机<br><li>FALSE：表示在正常关机失败后不进行强制关机<br><br>默认取值：FALSE。<br><br>强制关机的效果等同于关闭物理计算机的电源开关。强制关机可能会导致数据丢失或文件系统损坏，请仅在服务器不能正常关机时使用。"
      }
    ],
    "desc": "本接口 (ResetInstancesPassword) 用于将实例操作系统的密码重置为用户指定的密码。\n\n*如果是修改系统管理云密码：实例的操作系统不同，管理员帐号也会不一样(`Windows`为`Administrator`，`Ubuntu`为`ubuntu`，其它系统为`root`)。\n* 重置处于运行中状态的实例密码，需要设置关机参数`ForceStop`为`TRUE`。如果没有显式指定强制关机参数，则只有处于关机状态的实例才允许执行重置密码操作。\n* 支持批量操作。将多个实例操作系统的密码重置为相同的密码。每次请求批量实例的上限为100。\n* 实例操作结果可以通过调用 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728#.E7.A4.BA.E4.BE.8B3-.E6.9F.A5.E8.AF.A2.E5.AE.9E.E4.BE.8B.E7.9A.84.E6.9C.80.E6.96.B0.E6.93.8D.E4.BD.9C.E6.83.85.E5.86.B5) 接口查询，如果实例的最新操作状态(LatestOperationState)为“SUCCESS”，则代表操作成功。"
  },
  "ModifyInstancesRenewFlag": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "一个或多个待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728) API返回值中的`InstanceId`获取。每次请求允许操作的实例数量上限是100。"
      },
      {
        "name": "RenewFlag",
        "desc": "自动续费标识。取值范围：<br><li>NOTIFY_AND_AUTO_RENEW：通知过期且自动续费<br><li>NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费<br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费<br><br>若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，实例到期后将按月自动续费。"
      }
    ],
    "desc": "本接口 (ModifyInstancesRenewFlag) 用于修改包年包月实例续费标识。\n\n* 实例被标识为自动续费后，每次在实例到期时，会自动续费一个月。\n* 支持批量操作。每次请求批量实例的上限为100。\n* 实例操作结果可以通过调用 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728#.E7.A4.BA.E4.BE.8B3-.E6.9F.A5.E8.AF.A2.E5.AE.9E.E4.BE.8B.E7.9A.84.E6.9C.80.E6.96.B0.E6.93.8D.E4.BD.9C.E6.83.85.E5.86.B5) 接口查询，如果实例的最新操作状态(LatestOperationState)为“SUCCESS”，则代表操作成功。"
  },
  "PurchaseReservedInstancesOffering": {
    "params": [
      {
        "name": "InstanceCount",
        "desc": "购买预留实例计费数量"
      },
      {
        "name": "ReservedInstancesOfferingId",
        "desc": "预留实例计费配置ID"
      },
      {
        "name": "DryRun",
        "desc": "试运行"
      },
      {
        "name": "ClientToken",
        "desc": "用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。<br>更多详细信息请参阅：如何保证幂等性"
      }
    ],
    "desc": "本接口(PurchaseReservedInstancesOffering)用于用户购买一个或者多个指定配置的预留实例"
  },
  "ResizeInstanceDisks": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728)接口返回值中的`InstanceId`获取。"
      },
      {
        "name": "DataDisks",
        "desc": "待扩容的数据盘配置信息。只支持扩容非弹性数据盘（[`DescribeDisks`](https://cloud.tencent.com/document/api/362/16315)接口返回值中的`Portable`为`false`表示非弹性），且[数据盘类型](/document/api/213/9452#block_device)为：`CLOUD_BASIC`、`CLOUD_PREMIUM`、`CLOUD_SSD`。数据盘容量单位：GB。最小扩容步长：10G。关于数据盘类型的选择请参考[硬盘产品简介](https://cloud.tencent.com/document/product/362/2353)。可选数据盘类型受到实例类型`InstanceType`限制。另外允许扩容的最大容量也因数据盘类型的不同而有所差异。"
      },
      {
        "name": "ForceStop",
        "desc": "是否对运行中的实例选择强制关机。建议对运行中的实例先手动关机，然后再重置用户密码。取值范围：<br><li>TRUE：表示在正常关机失败后进行强制关机<br><li>FALSE：表示在正常关机失败后不进行强制关机<br><br>默认取值：FALSE。<br><br>强制关机的效果等同于关闭物理计算机的电源开关。强制关机可能会导致数据丢失或文件系统损坏，请仅在服务器不能正常关机时使用。"
      }
    ],
    "desc": "本接口 (ResizeInstanceDisks) 用于扩容实例的数据盘。\n\n* 目前只支持扩容非弹性数据盘（[`DescribeDisks`](https://cloud.tencent.com/document/api/362/16315)接口返回值中的`Portable`为`false`表示非弹性），且[数据盘类型](https://cloud.tencent.com/document/api/213/15753#DataDisk)为：`CLOUD_BASIC`、`CLOUD_PREMIUM`、`CLOUD_SSD`和[CDH](https://cloud.tencent.com/document/product/416)实例的`LOCAL_BASIC`、`LOCAL_SSD`类型数据盘。\n* 对于包年包月实例，使用该接口会涉及扣费，请确保账户余额充足。可通过[`DescribeAccountBalance`](https://cloud.tencent.com/document/product/555/20253)接口查询账户余额。\n* 目前只支持扩容一块数据盘。\n* 实例操作结果可以通过调用 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728#.E7.A4.BA.E4.BE.8B3-.E6.9F.A5.E8.AF.A2.E5.AE.9E.E4.BE.8B.E7.9A.84.E6.9C.80.E6.96.B0.E6.93.8D.E4.BD.9C.E6.83.85.E5.86.B5) 接口查询，如果实例的最新操作状态(LatestOperationState)为“SUCCESS”，则代表操作成功。"
  },
  "DescribeReservedInstances": {
    "params": [
      {
        "name": "DryRun",
        "desc": "试运行。默认为 false。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。"
      },
      {
        "name": "Filters",
        "desc": "<li><strong>zone</strong></li>\n<p style=\"padding-left: 30px;\">按照预留实例计费可购买的【<strong>可用区</strong>】进行过滤。形如：ap-guangzhou-1。</p><p style=\"padding-left: 30px;\">类型：String</p><p style=\"padding-left: 30px;\">必选：否</p><p style=\"padding-left: 30px;\">可选项：<a href=\"https://cloud.tencent.com/document/product/213/6091\">可用区列表</a></p>\n<li><strong>duration</strong></li>\n<p style=\"padding-left: 30px;\">按照预留实例计费【<strong>有效期</strong>】即预留实例计费购买时长进行过滤。形如：31536000。</p><p style=\"padding-left: 30px;\">类型：Integer</p><p style=\"padding-left: 30px;\">计量单位：秒</p><p style=\"padding-left: 30px;\">必选：否</p><p style=\"padding-left: 30px;\">可选项：31536000 (1年) | 94608000（3年）</p>\n<li><strong>instance-type</strong></li>\n<p style=\"padding-left: 30px;\">按照【<strong>预留实例计费类型</strong>】进行过滤。形如：S3.MEDIUM4。</p><p style=\"padding-left: 30px;\">类型：String</p><p style=\"padding-left: 30px;\">必选：否</p><p style=\"padding-left: 30px;\">可选项：<a href=\"https://cloud.tencent.com/document/product/213/11518\">预留实例计费类型列表</a></p>\n<li><strong>offering-type</strong></li>\n<p style=\"padding-left: 30px;\">按照【<strong>付款类型</strong>】进行过滤。形如：All Upfront (预付全部费用)。</p><p style=\"padding-left: 30px;\">类型：String</p><p style=\"padding-left: 30px;\">必选：否</p><p style=\"padding-left: 30px;\">可选项：All Upfront (预付全部费用)</p>\n<li><strong>product-description</strong></li>\n<p style=\"padding-left: 30px;\">按照预留实例计费的【<strong>平台描述</strong>】（即操作系统）进行过滤。形如：linux。</p><p style=\"padding-left: 30px;\">类型：String</p><p style=\"padding-left: 30px;\">必选：否</p><p style=\"padding-left: 30px;\">可选项：linux</p>\n<li><strong>reserved-instances-id</strong></li>\n<p style=\"padding-left: 30px;\">按照已购买【<strong>预留实例计费ID</strong>】进行过滤。形如：650c138f-ae7e-4750-952a-96841d6e9fc1。</p><p style=\"padding-left: 30px;\">类型：String</p><p style=\"padding-left: 30px;\">必选：否</p>\n<li><strong>state</strong></li>\n<p style=\"padding-left: 30px;\">按照已购买【<strong>预留实例计费状态</strong>】进行过滤。形如：active。</p><p style=\"padding-left: 30px;\">类型：String</p><p style=\"padding-left: 30px;\">必选：否</p><p style=\"padding-left: 30px;\">可选项：active (以创建) | pending (等待被创建) | retired (过期)</p>\n每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。"
      }
    ],
    "desc": "本接口(DescribeReservedInstances)可提供列出用户已购买的预留实例"
  },
  "DescribeZones": {
    "params": [],
    "desc": "本接口(DescribeZones)用于查询可用区信息。"
  },
  "DescribeImageQuota": {
    "params": [],
    "desc": "本接口(DescribeImageQuota)用于查询用户帐号的镜像配额。"
  },
  "AssociateSecurityGroups": {
    "params": [
      {
        "name": "SecurityGroupIds",
        "desc": "要绑定的`安全组ID`，类似sg-efil73jd，只支持绑定单个安全组。"
      },
      {
        "name": "InstanceIds",
        "desc": "被绑定的`实例ID`，类似ins-lesecurk，支持指定多个实例，每次请求批量实例的上限为100。"
      }
    ],
    "desc": "本接口 (AssociateSecurityGroups) 用于绑定安全组到指定实例。\n* 实例操作结果可以通过调用 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728#.E7.A4.BA.E4.BE.8B3-.E6.9F.A5.E8.AF.A2.E5.AE.9E.E4.BE.8B.E7.9A.84.E6.9C.80.E6.96.B0.E6.93.8D.E4.BD.9C.E6.83.85.E5.86.B5) 接口查询，如果实例的最新操作状态(LatestOperationState)为“SUCCESS”，则代表操作成功。"
  },
  "ResetInstancesType": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "一个或多个待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728)接口返回值中的`InstanceId`获取。本接口目前仅支持每次操作1个实例。"
      },
      {
        "name": "InstanceType",
        "desc": "实例机型。不同实例机型指定了不同的资源规格，具体取值可通过调用接口[`DescribeInstanceTypeConfigs`](https://cloud.tencent.com/document/api/213/15749)来获得最新的规格表或参见[实例类型](https://cloud.tencent.com/document/product/213/11518)描述。"
      },
      {
        "name": "ForceStop",
        "desc": "是否对运行中的实例选择强制关机。建议对运行中的实例先手动关机。取值范围：<br><li>TRUE：表示在正常关机失败后进行强制关机<br><li>FALSE：表示在正常关机失败后不进行强制关机<br><br>默认取值：FALSE。<br><br>强制关机的效果等同于关闭物理计算机的电源开关。强制关机可能会导致数据丢失或文件系统损坏，请仅在服务器不能正常关机时使用。"
      }
    ],
    "desc": "本接口 (ResetInstancesType) 用于调整实例的机型。\n* 目前只支持[系统盘类型](/document/api/213/9452#block_device)是`CLOUD_BASIC`、`CLOUD_PREMIUM`、`CLOUD_SSD`类型的实例使用该接口进行机型调整。\n* 目前不支持[CDH](https://cloud.tencent.com/document/product/416)实例使用该接口调整机型。对于包年包月实例，使用该接口会涉及扣费，请确保账户余额充足。可通过[`DescribeAccountBalance`](https://cloud.tencent.com/document/product/555/20253)接口查询账户余额。\n* 本接口为异步接口，调整实例配置请求发送成功后会返回一个RequestId，此时操作并未立即完成。实例操作结果可以通过调用 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728#.E7.A4.BA.E4.BE.8B3-.E6.9F.A5.E8.AF.A2.E5.AE.9E.E4.BE.8B.E7.9A.84.E6.9C.80.E6.96.B0.E6.93.8D.E4.BD.9C.E6.83.85.E5.86.B5) 接口查询，如果实例的最新操作状态(LatestOperationState)为“SUCCESS”，则代表调整实例配置操作成功。"
  },
  "ModifyImageAttribute": {
    "params": [
      {
        "name": "ImageId",
        "desc": "镜像ID，形如`img-gvbnzy6f`。镜像ID可以通过如下方式获取：<br><li>通过[DescribeImages](https://cloud.tencent.com/document/api/213/15715)接口返回的`ImageId`获取。<br><li>通过[镜像控制台](https://console.cloud.tencent.com/cvm/image)获取。"
      },
      {
        "name": "ImageName",
        "desc": "设置新的镜像名称；必须满足下列限制：<br> <li> 不得超过20个字符。<br> <li> 镜像名称不能与已有镜像重复。"
      },
      {
        "name": "ImageDescription",
        "desc": "设置新的镜像描述；必须满足下列限制：<br> <li> 不得超过60个字符。"
      }
    ],
    "desc": "本接口（ModifyImageAttribute）用于修改镜像属性。\n\n* 已分享的镜像无法修改属性。"
  },
  "DescribeInstancesOperationLimit": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "按照一个或者多个实例ID查询，可通过[DescribeInstances](https://cloud.tencent.com/document/api/213/15728)API返回值中的InstanceId获取。实例ID形如：ins-xxxxxxxx。（此参数的具体格式可参考API[简介](https://cloud.tencent.com/document/api/213/15688)的ids.N一节）。每次请求的实例的上限为100。"
      },
      {
        "name": "Operation",
        "desc": "实例操作。\n<li> INSTANCE_DEGRADE：实例降配操作</li>"
      }
    ],
    "desc": "本接口（DescribeInstancesOperationLimit）用于查询实例操作限制。\n\n* 目前支持调整配置操作限制次数查询。"
  },
  "InquiryPriceResetInstancesType": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "一个或多个待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728)接口返回值中的`InstanceId`获取。本接口每次请求批量实例的上限为1。"
      },
      {
        "name": "InstanceType",
        "desc": "实例机型。不同实例机型指定了不同的资源规格，具体取值可参见附表[实例资源规格](https://cloud.tencent.com/document/product/213/11518)对照表，也可以调用查询[实例资源规格列表](https://cloud.tencent.com/document/product/213/15749)接口获得最新的规格表。"
      }
    ],
    "desc": "本接口 (InquiryPriceResetInstancesType) 用于调整实例的机型询价。\n\n* 目前只支持[系统盘类型](https://cloud.tencent.com/document/product/213/15753#SystemDisk)是`CLOUD_BASIC`、`CLOUD_PREMIUM`、`CLOUD_SSD`类型的实例使用该接口进行调整机型询价。\n* 目前不支持[CDH](https://cloud.tencent.com/document/product/416)实例使用该接口调整机型询价。\n* 对于包年包月实例，使用该接口会涉及扣费，请确保账户余额充足。可通过[`DescribeAccountBalance`](https://cloud.tencent.com/document/product/555/20253)接口查询账户余额。"
  },
  "StopInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "一个或多个待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728)接口返回值中的`InstanceId`获取。每次请求批量实例的上限为100。"
      },
      {
        "name": "ForceStop",
        "desc": "是否在正常关闭失败后选择强制关闭实例。取值范围：<br><li>TRUE：表示在正常关闭失败后进行强制关闭<br><li>FALSE：表示在正常关闭失败后不进行强制关闭<br><br>默认取值：FALSE。"
      },
      {
        "name": "StopType",
        "desc": "实例的关闭模式。取值范围：<br><li>SOFT_FIRST：表示在正常关闭失败后进行强制关闭<br><li>HARD：直接强制关闭<br><li>SOFT：仅软关机<br>默认取值：SOFT。"
      },
      {
        "name": "StoppedMode",
        "desc": "按量计费实例关机收费模式。\n取值范围：<br><li>KEEP_CHARGING：关机继续收费<br><li>STOP_CHARGING：关机停止收费<br>默认取值：KEEP_CHARGING。\n该参数只针对部分按量计费云硬盘实例生效，详情参考[按量计费实例关机不收费说明](https://cloud.tencent.com/document/product/213/19918)"
      }
    ],
    "desc": "本接口 (StopInstances) 用于关闭一个或多个实例。\n\n* 只有状态为`RUNNING`的实例才可以进行此操作。\n* 接口调用成功时，实例会进入`STOPPING`状态；关闭实例成功时，实例会进入`STOPPED`状态。\n* 支持强制关闭。强制关机的效果等同于关闭物理计算机的电源开关。强制关机可能会导致数据丢失或文件系统损坏，请仅在服务器不能正常关机时使用。\n* 支持批量操作。每次请求批量实例的上限为100。\n* 本接口为异步接口，关闭实例请求发送成功后会返回一个RequestId，此时操作并未立即完成。实例操作结果可以通过调用 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728#.E7.A4.BA.E4.BE.8B3-.E6.9F.A5.E8.AF.A2.E5.AE.9E.E4.BE.8B.E7.9A.84.E6.9C.80.E6.96.B0.E6.93.8D.E4.BD.9C.E6.83.85.E5.86.B5) 接口查询，如果实例的最新操作状态(LatestOperationState)为“SUCCESS”，则代表关闭实例操作成功。"
  },
  "ModifyHostsAttribute": {
    "params": [
      {
        "name": "HostIds",
        "desc": "一个或多个待操作的CDH实例ID。"
      },
      {
        "name": "HostName",
        "desc": "CDH实例显示名称。可任意命名，但不得超过60个字符。"
      },
      {
        "name": "RenewFlag",
        "desc": "自动续费标识。取值范围：<br><li>NOTIFY_AND_AUTO_RENEW：通知过期且自动续费<br><li>NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费<br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费<br><br>若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，实例到期后将按月自动续费。"
      },
      {
        "name": "ProjectId",
        "desc": "项目ID。项目可以使用[AddProject](https://cloud.tencent.com/doc/api/403/4398)接口创建。可通过[`DescribeProject`](https://cloud.tencent.com/document/product/378/4400) API返回值中的`projectId`获取。后续使用[DescribeHosts](https://cloud.tencent.com/document/api/213/16474)接口查询实例时，项目ID可用于过滤结果。"
      }
    ],
    "desc": "本接口（ModifyHostsAttribute）用于修改CDH实例的属性，如实例名称和续费标记等。参数HostName和RenewFlag必须设置其中一个，但不能同时设置。"
  },
  "DescribeImportImageOs": {
    "params": [],
    "desc": "查看可以导入的镜像操作系统信息。"
  },
  "DescribeInstanceVncUrl": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "一个操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728) API返回值中的`InstanceId`获取。"
      }
    ],
    "desc": "本接口 ( DescribeInstanceVncUrl ) 用于查询实例管理终端地址，获取的地址可用于实例的 VNC 登录。\n\n* 处于 `STOPPED` 状态的机器无法使用此功能。\n* 管理终端地址的有效期为 15 秒，调用接口成功后如果 15 秒内不使用该链接进行访问，管理终端地址自动失效，您需要重新查询。\n* 管理终端地址一旦被访问，将自动失效，您需要重新查询。\n* 如果连接断开，每分钟内重新连接的次数不能超过 30 次。\n* 获取到 `InstanceVncUrl` 后，您需要在链接 <https://img.qcloud.com/qcloud/app/active_vnc/index.html?> 末尾加上参数 `InstanceVncUrl=xxxx`  。\n\n  - 参数 `InstanceVncUrl` ：调用接口成功后会返回的 `InstanceVncUrl` 的值。\n\n    最后组成的 URL 格式如下：\n\n```\nhttps://img.qcloud.com/qcloud/app/active_vnc/index.html?InstanceVncUrl=wss%3A%2F%2Fbjvnc.qcloud.com%3A26789%2Fvnc%3Fs%3DaHpjWnRVMFNhYmxKdDM5MjRHNlVTSVQwajNUSW0wb2tBbmFtREFCTmFrcy8vUUNPMG0wSHZNOUUxRm5PMmUzWmFDcWlOdDJIbUJxSTZDL0RXcHZxYnZZMmRkWWZWcEZia2lyb09XMzdKNmM9\n```\n"
  },
  "ResetInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID。可通过 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) API返回值中的`InstanceId`获取。"
      },
      {
        "name": "ImageId",
        "desc": "指定有效的[镜像](https://cloud.tencent.com/document/product/213/4940)ID，格式形如`img-xxx`。镜像类型分为四种：<br/><li>公共镜像</li><li>自定义镜像</li><li>共享镜像</li><li>服务市场镜像</li><br/>可通过以下方式获取可用的镜像ID：<br/><li>`公共镜像`、`自定义镜像`、`共享镜像`的镜像ID可通过登录[控制台](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE)查询；`服务镜像市场`的镜像ID可通过[云市场](https://market.cloud.tencent.com/list)查询。</li><li>通过调用接口 [DescribeImages](https://cloud.tencent.com/document/api/213/15715) ，取返回信息中的`ImageId`字段。</li>\n<br>默认取值：默认使用当前镜像。"
      },
      {
        "name": "SystemDisk",
        "desc": "实例系统盘配置信息。系统盘为云盘的实例可以通过该参数指定重装后的系统盘大小来实现对系统盘的扩容操作，若不指定大小且原系统盘大小小于镜像大小，则会自动扩容，产生多余的磁盘费用。系统盘大小只支持扩容不支持缩容；重装只支持修改系统盘的大小，不能修改系统盘的类型。"
      },
      {
        "name": "LoginSettings",
        "desc": "实例登录设置。通过该参数可以设置实例的登录方式密码、密钥或保持镜像的原始登录设置。默认情况下会随机生成密码，并以站内信方式知会到用户。"
      },
      {
        "name": "EnhancedService",
        "desc": "增强服务。通过该参数可以指定是否开启云安全、云监控等服务。若不指定该参数，则默认开启云监控、云安全服务。"
      },
      {
        "name": "HostName",
        "desc": "重装系统时，可以指定修改实例的主机名。<br><li>点号（.）和短横线（-）不能作为 HostName 的首尾字符，不能连续使用。<br><li>Windows 实例：名字符长度为[2, 15]，允许字母（不限制大小写）、数字和短横线（-）组成，不支持点号（.），不能全是数字。<br><li>其他类型（Linux 等）实例：字符长度为[2, 60]，允许支持多个点号，点之间为一段，每段允许字母（不限制大小写）、数字和短横线（-）组成。"
      }
    ],
    "desc": "本接口 (ResetInstance) 用于重装指定实例上的操作系统。\n\n* 如果指定了`ImageId`参数，则使用指定的镜像重装；否则按照当前实例使用的镜像进行重装。\n* 系统盘将会被格式化，并重置；请确保系统盘中无重要文件。\n* `Linux`和`Windows`系统互相切换时，该实例系统盘`ID`将发生变化，系统盘关联快照将无法回滚、恢复数据。\n* 密码不指定将会通过站内信下发随机密码。\n* 目前只支持[系统盘类型](https://cloud.tencent.com/document/api/213/9452#SystemDisk)是`CLOUD_BASIC`、`CLOUD_PREMIUM`、`CLOUD_SSD`类型的实例使用该接口实现`Linux`和`Windows`操作系统切换。\n* 目前不支持境外地域的实例使用该接口实现`Linux`和`Windows`操作系统切换。\n* 实例操作结果可以通过调用 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728#.E7.A4.BA.E4.BE.8B3-.E6.9F.A5.E8.AF.A2.E5.AE.9E.E4.BE.8B.E7.9A.84.E6.9C.80.E6.96.B0.E6.93.8D.E4.BD.9C.E6.83.85.E5.86.B5) 接口查询，如果实例的最新操作状态(LatestOperationState)为“SUCCESS”，则代表操作成功。"
  },
  "SyncImages": {
    "params": [
      {
        "name": "ImageIds",
        "desc": "镜像ID列表 ，镜像ID可以通过如下方式获取：<br><li>通过[DescribeImages](https://cloud.tencent.com/document/api/213/15715)接口返回的`ImageId`获取。<br><li>通过[镜像控制台](https://console.cloud.tencent.com/cvm/image)获取。<br>镜像ID必须满足限制：<br><li>镜像ID对应的镜像状态必须为`NORMAL`。<br><li>镜像大小小于50GB。<br>镜像状态请参考[镜像数据表](https://cloud.tencent.com/document/product/213/15753#Image)。"
      },
      {
        "name": "DestinationRegions",
        "desc": "目的同步地域列表；必须满足限制：<br><li>不能为源地域，<br><li>必须是一个合法的Region。<br><li>暂不支持部分地域同步。<br>具体地域参数请参考[Region](https://cloud.tencent.com/document/product/213/6091)。"
      }
    ],
    "desc": "本接口（SyncImages）用于将自定义镜像同步到其它地区。\n\n* 该接口每次调用只支持同步一个镜像。\n* 该接口支持多个同步地域。\n* 单个帐号在每个地域最多支持存在10个自定义镜像。"
  },
  "DeleteDisasterRecoverGroups": {
    "params": [
      {
        "name": "DisasterRecoverGroupIds",
        "desc": "分散置放群组ID列表，可通过[DescribeDisasterRecoverGroups](https://cloud.tencent.com/document/api/213/17810)接口获取。每次请求允许操作的分散置放群组数量上限是100。"
      }
    ],
    "desc": "本接口 (DeleteDisasterRecoverGroups)用于删除[分散置放群组](https://cloud.tencent.com/document/product/213/15486)。只有空的置放群组才能被删除，非空的群组需要先销毁组内所有云服务器，才能执行删除操作，不然会产生删除置放群组失败的错误。"
  },
  "TerminateInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "一个或多个待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728)接口返回值中的`InstanceId`获取。每次请求批量实例的上限为100。"
      }
    ],
    "desc": "本接口 (TerminateInstances) 用于主动退还实例。\n\n* 不再使用的实例，可通过本接口主动退还。\n* 按量计费的实例通过本接口可直接退还；包年包月实例如符合[退还规则](https://cloud.tencent.com/document/product/213/9711)，也可通过本接口主动退还。\n* 包年包月实例首次调用本接口，实例将被移至回收站，再次调用本接口，实例将被销毁，且不可恢复。按量计费实例调用本接口将被直接销毁\n* 支持批量操作，每次请求批量实例的上限为100。"
  },
  "RenewInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "一个或多个待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728)接口返回值中的`InstanceId`获取。每次请求批量实例的上限为100。"
      },
      {
        "name": "InstanceChargePrepaid",
        "desc": "预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的续费时长、是否设置自动续费等属性。包年包月实例该参数为必传参数。"
      },
      {
        "name": "RenewPortableDataDisk",
        "desc": "是否续费弹性数据盘。取值范围：<br><li>TRUE：表示续费包年包月实例同时续费其挂载的弹性数据盘<br><li>FALSE：表示续费包年包月实例同时不再续费其挂载的弹性数据盘<br><br>默认取值：TRUE。"
      }
    ],
    "desc": "本接口 (RenewInstances) 用于续费包年包月实例。\n\n* 只支持操作包年包月实例。\n* 续费时请确保账户余额充足。可通过[`DescribeAccountBalance`](https://cloud.tencent.com/document/product/555/20253)接口查询账户余额。\n* 实例操作结果可以通过调用 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728#.E7.A4.BA.E4.BE.8B3-.E6.9F.A5.E8.AF.A2.E5.AE.9E.E4.BE.8B.E7.9A.84.E6.9C.80.E6.96.B0.E6.93.8D.E4.BD.9C.E6.83.85.E5.86.B5) 接口查询，如果实例的最新操作状态(LatestOperationState)为“SUCCESS”，则代表操作成功。"
  },
  "DescribeZoneInstanceConfigInfos": {
    "params": [
      {
        "name": "Filters",
        "desc": "<li><strong>zone</strong></li>\n<p style=\"padding-left: 30px;\">按照【<strong>可用区</strong>】进行过滤。可用区形如：ap-guangzhou-1。</p><p style=\"padding-left: 30px;\">类型：String</p><p style=\"padding-left: 30px;\">必选：否</p><p style=\"padding-left: 30px;\">可选项：<a href=\"https://cloud.tencent.com/document/product/213/6091\">可用区列表</a></p>\n<li><strong>instance-family</strong></li>\n<p style=\"padding-left: 30px;\">按照【<strong>实例机型系列</strong>】进行过滤。实例机型系列形如：S1、I1、M1等。</p><p style=\"padding-left: 30px;\">类型：Integer</p><p style=\"padding-left: 30px;\">必选：否</p>\n<li><strong>instance-type</strong></li>\n<p style=\"padding-left: 30px;\">按照【<strong>实例机型</strong>】进行过滤。不同实例机型指定了不同的资源规格，具体取值可通过调用接口 [DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/product/213/15749) 来获得最新的规格表或参见[实例类型](https://cloud.tencent.com/document/product/213/11518)描述。若不指定该参数，则默认机型为S1.SMALL1。</p><p style=\"padding-left: 30px;\">类型：String</p><p style=\"padding-left: 30px;\">必选：否</p>\n<li><strong>instance-charge-type</strong></li>\n<p style=\"padding-left: 30px;\">按照【<strong>实例计费模式</strong>】进行过滤。(PREPAID：表示预付费，即包年包月 | POSTPAID_BY_HOUR：表示后付费，即按量计费 | CDHPAID：表示[CDH](https://cloud.tencent.com/document/product/416)付费，即只对[CDH](https://cloud.tencent.com/document/product/416)计费，不对[CDH](https://cloud.tencent.com/document/product/416)上的实例计费。)</p><p style=\"padding-left: 30px;\">类型：String</p><p style=\"padding-left: 30px;\">必选：否</p>\n每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。"
      }
    ],
    "desc": "本接口(DescribeZoneInstanceConfigInfos) 获取可用区的机型信息。"
  },
  "ModifyInstancesProject": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "一个或多个待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728) API返回值中的`InstanceId`获取。每次请求允许操作的实例数量上限是100。"
      },
      {
        "name": "ProjectId",
        "desc": "项目ID。项目可以使用[AddProject](https://cloud.tencent.com/doc/api/403/4398)接口创建。可通过[`DescribeProject`](https://cloud.tencent.com/document/product/378/4400) API返回值中的`projectId`获取。后续使用[DescribeInstances](https://cloud.tencent.com/document/api/213/15728)接口查询实例时，项目ID可用于过滤结果。"
      }
    ],
    "desc": "本接口 (ModifyInstancesProject) 用于修改实例所属项目。\n\n* 项目为一个虚拟概念，用户可以在一个账户下面建立多个项目，每个项目中管理不同的资源；将多个不同实例分属到不同项目中，后续使用 [`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728)接口查询实例，项目ID可用于过滤结果。\n* 绑定负载均衡的实例不支持修改实例所属项目，请先使用[`DeregisterInstancesFromLoadBalancer`](https://cloud.tencent.com/document/api/214/1258)接口解绑负载均衡。\n[^_^]: # ( 修改实例所属项目会自动解关联实例原来关联的安全组，修改完成后可使用[`ModifyInstancesAttribute`](https://cloud.tencent.com/document/api/213/15739)接口关联安全组。)\n* 支持批量操作。每次请求批量实例的上限为100。\n* 实例操作结果可以通过调用 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728#.E7.A4.BA.E4.BE.8B3-.E6.9F.A5.E8.AF.A2.E5.AE.9E.E4.BE.8B.E7.9A.84.E6.9C.80.E6.96.B0.E6.93.8D.E4.BD.9C.E6.83.85.E5.86.B5) 接口查询，如果实例的最新操作状态(LatestOperationState)为“SUCCESS”，则代表操作成功。"
  },
  "ModifyInstancesChargeType": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "一个或多个待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728)接口返回值中的`InstanceId`获取。每次请求批量实例的上限为100。"
      },
      {
        "name": "InstanceChargeType",
        "desc": "实例[计费类型](https://cloud.tencent.com/document/product/213/2180)。<br><li>PREPAID：预付费，即包年包月。"
      },
      {
        "name": "InstanceChargePrepaid",
        "desc": "预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。"
      }
    ],
    "desc": "本接口 (ModifyInstancesChargeType) 用于切换实例的计费模式。\n\n* 只支持从 `POSTPAID_BY_HOUR` 计费模式切换为`PREPAID`计费模式。\n* 关机不收费的实例、`BC1`和`BS1`机型族的实例、设置定时销毁的实例不支持该操作。\n* 实例操作结果可以通过调用 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728#.E7.A4.BA.E4.BE.8B3-.E6.9F.A5.E8.AF.A2.E5.AE.9E.E4.BE.8B.E7.9A.84.E6.9C.80.E6.96.B0.E6.93.8D.E4.BD.9C.E6.83.85.E5.86.B5) 接口查询，如果实例的最新操作状态(LatestOperationState)为“SUCCESS”，则代表操作成功。"
  },
  "RenewHosts": {
    "params": [
      {
        "name": "HostIds",
        "desc": "一个或多个待操作的CDH实例ID。每次请求的CDH实例的上限为100。"
      },
      {
        "name": "HostChargePrepaid",
        "desc": "预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。"
      }
    ],
    "desc": "本接口 (RenewHosts) 用于续费包年包月CDH实例。\n\n* 只支持操作包年包月实例，否则操作会以特定[错误码](#6.-.E9.94.99.E8.AF.AF.E7.A0.81)返回。\n* 续费时请确保账户余额充足。可通过[`DescribeAccountBalance`](https://cloud.tencent.com/document/product/555/20253)接口查询账户余额。"
  },
  "DescribeDisasterRecoverGroups": {
    "params": [
      {
        "name": "DisasterRecoverGroupIds",
        "desc": "分散置放群组ID列表。每次请求允许操作的分散置放群组数量上限是100。"
      },
      {
        "name": "Name",
        "desc": "分散置放群组名称，支持模糊匹配。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。"
      }
    ],
    "desc": "本接口 (DescribeDisasterRecoverGroups)用于查询[分散置放群组](https://cloud.tencent.com/document/product/213/15486)信息。"
  },
  "StartInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "一个或多个待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728)接口返回值中的`InstanceId`获取。每次请求批量实例的上限为100。"
      }
    ],
    "desc": "本接口 (StartInstances) 用于启动一个或多个实例。\n\n* 只有状态为`STOPPED`的实例才可以进行此操作。\n* 接口调用成功时，实例会进入`STARTING`状态；启动实例成功时，实例会进入`RUNNING`状态。\n* 支持批量操作。每次请求批量实例的上限为100。\n* 本接口为异步接口，启动实例请求发送成功后会返回一个RequestId，此时操作并未立即完成。实例操作结果可以通过调用 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728#.E7.A4.BA.E4.BE.8B3-.E6.9F.A5.E8.AF.A2.E5.AE.9E.E4.BE.8B.E7.9A.84.E6.9C.80.E6.96.B0.E6.93.8D.E4.BD.9C.E6.83.85.E5.86.B5) 接口查询，如果实例的最新操作状态(LatestOperationState)为“SUCCESS”，则代表启动实例操作成功。"
  },
  "ResetInstancesInternetMaxBandwidth": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "一个或多个待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/9388)接口返回值中的 `InstanceId` 获取。 每次请求批量实例的上限为100。当调整 `BANDWIDTH_PREPAID` 和 `BANDWIDTH_POSTPAID_BY_HOUR` 计费方式的带宽时，只支持一个实例。"
      },
      {
        "name": "InternetAccessible",
        "desc": "公网出带宽配置。不同机型带宽上限范围不一致，具体限制详见带宽限制对账表。暂时只支持 `InternetMaxBandwidthOut` 参数。"
      },
      {
        "name": "StartTime",
        "desc": "带宽生效的起始时间。格式：`YYYY-MM-DD`，例如：`2016-10-30`。起始时间不能早于当前时间。如果起始时间是今天则新设置的带宽立即生效。该参数只对包年包月带宽有效，其他模式带宽不支持该参数，否则接口会以相应错误码返回。"
      },
      {
        "name": "EndTime",
        "desc": "带宽生效的终止时间。格式： `YYYY-MM-DD` ，例如：`2016-10-30` 。新设置的带宽的有效期包含终止时间此日期。终止时间不能晚于包年包月实例的到期时间。实例的到期时间可通过 [`DescribeInstances`](https://cloud.tencent.com/document/api/213/9388)接口返回值中的`ExpiredTime`获取。该参数只对包年包月带宽有效，其他模式带宽不支持该参数，否则接口会以相应错误码返回。"
      }
    ],
    "desc": "本接口 (ResetInstancesInternetMaxBandwidth) 用于调整实例公网带宽上限。\n\n* 不同机型带宽上限范围不一致，具体限制详见[公网带宽上限](https://cloud.tencent.com/document/product/213/12523)。\n* 对于 `BANDWIDTH_PREPAID` 计费方式的带宽，需要输入参数 `StartTime` 和 `EndTime` ，指定调整后的带宽的生效时间段。在这种场景下目前不支持调小带宽，会涉及扣费，请确保账户余额充足。可通过 [`DescribeAccountBalance`](https://cloud.tencent.com/document/product/555/20253) 接口查询账户余额。\n* 对于 `TRAFFIC_POSTPAID_BY_HOUR` 、 `BANDWIDTH_POSTPAID_BY_HOUR` 和 `BANDWIDTH_PACKAGE` 计费方式的带宽，使用该接口调整带宽上限是实时生效的，可以在带宽允许的范围内调大或者调小带宽，不支持输入参数 `StartTime` 和 `EndTime` 。\n* 接口不支持调整 `BANDWIDTH_POSTPAID_BY_MONTH` 计费方式的带宽。\n* 接口不支持批量调整 `BANDWIDTH_PREPAID` 和 `BANDWIDTH_POSTPAID_BY_HOUR` 计费方式的带宽。\n* 接口不支持批量调整混合计费方式的带宽。例如不支持同时调整 `TRAFFIC_POSTPAID_BY_HOUR` 和 `BANDWIDTH_PACKAGE` 计费方式的带宽。\n* 实例操作结果可以通过调用 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728#.E7.A4.BA.E4.BE.8B3-.E6.9F.A5.E8.AF.A2.E5.AE.9E.E4.BE.8B.E7.9A.84.E6.9C.80.E6.96.B0.E6.93.8D.E4.BD.9C.E6.83.85.E5.86.B5) 接口查询，如果实例的最新操作状态(LatestOperationState)为“SUCCESS”，则代表操作成功。"
  },
  "DescribeKeyPairs": {
    "params": [
      {
        "name": "KeyIds",
        "desc": "密钥对ID，密钥对ID形如：`skey-11112222`（此接口支持同时传入多个ID进行过滤。此参数的具体格式可参考 API [简介](https://cloud.tencent.com/document/api/213/15688)的 `id.N` 一节）。参数不支持同时指定 `KeyIds` 和 `Filters`。密钥对ID可以通过登录[控制台](https://console.cloud.tencent.com/cvm/index)查询。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件。\n<li> project-id - Integer - 是否必填：否 -（过滤条件）按照项目ID过滤。可以通过[项目列表](https://console.cloud.tencent.com/project)查询项目ID，或者调用接口 [DescribeProject](https://cloud.tencent.com/document/api/378/4400)，取返回信息中的projectId获取项目ID。</li>\n<li> key-name - String - 是否必填：否 -（过滤条件）按照密钥对名称过滤。</li>参数不支持同时指定 `KeyIds` 和 `Filters`。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。关于 `Offset` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。返回数量，默认为20，最大值为100。关于 `Limit` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。关于 `Limit` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。"
      }
    ],
    "desc": "本接口 (DescribeKeyPairs) 用于查询密钥对信息。\n\n* 密钥对是通过一种算法生成的一对密钥，在生成的密钥对中，一个向外界公开，称为公钥；另一个用户自己保留，称为私钥。密钥对的公钥内容可以通过这个接口查询，但私钥内容系统不保留。"
  },
  "DescribeReservedInstancesOfferings": {
    "params": [
      {
        "name": "DryRun",
        "desc": "试运行, 默认为 false。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。"
      },
      {
        "name": "MaxDuration",
        "desc": "以最大有效期作为过滤参数。\n计量单位: 秒\n默认为 94608000。"
      },
      {
        "name": "MinDuration",
        "desc": "以最小有效期作为过滤参数。\n计量单位: 秒\n默认为 2592000。"
      },
      {
        "name": "Filters",
        "desc": "<li><strong>zone</strong></li>\n<p style=\"padding-left: 30px;\">按照预留实例计费可购买的【<strong>可用区</strong>】进行过滤。形如：ap-guangzhou-1。</p><p style=\"padding-left: 30px;\">类型：String</p><p style=\"padding-left: 30px;\">必选：否</p><p style=\"padding-left: 30px;\">可选项：<a href=\"https://cloud.tencent.com/document/product/213/6091\">可用区列表</a></p>\n<li><strong>duration</strong></li>\n<p style=\"padding-left: 30px;\">按照预留实例计费【<strong>有效期</strong>】即预留实例计费购买时长进行过滤。形如：31536000。</p><p style=\"padding-left: 30px;\">类型：Integer</p><p style=\"padding-left: 30px;\">计量单位：秒</p><p style=\"padding-left: 30px;\">必选：否</p><p style=\"padding-left: 30px;\">可选项：31536000 (1年) | 94608000（3年）</p>\n<li><strong>instance-type</strong></li>\n<p style=\"padding-left: 30px;\">按照【<strong>预留实例计费类型</strong>】进行过滤。形如：S3.MEDIUM4。</p><p style=\"padding-left: 30px;\">类型：String</p><p style=\"padding-left: 30px;\">必选：否</p><p style=\"padding-left: 30px;\">可选项：<a href=\"https://cloud.tencent.com/document/product/213/11518\">预留实例计费类型列表</a></p>\n<li><strong>offering-type</strong></li>\n<p style=\"padding-left: 30px;\">按照【<strong>付款类型</strong>】进行过滤。形如：All Upfront (预付全部费用)。</p><p style=\"padding-left: 30px;\">类型：String</p><p style=\"padding-left: 30px;\">必选：否</p><p style=\"padding-left: 30px;\">可选项：All Upfront (预付全部费用)</p>\n<li><strong>product-description</strong></li>\n<p style=\"padding-left: 30px;\">按照预留实例计费的【<strong>平台描述</strong>】（即操作系统）进行过滤。形如：linux。</p><p style=\"padding-left: 30px;\">类型：String</p><p style=\"padding-left: 30px;\">必选：否</p><p style=\"padding-left: 30px;\">可选项：linux</p>\n<li><strong>reserved-instances-offering-id</strong></li>\n<p style=\"padding-left: 30px;\">按照【<strong>预留实例计费配置ID</strong>】进行过滤。形如：650c138f-ae7e-4750-952a-96841d6e9fc1。</p><p style=\"padding-left: 30px;\">类型：String</p><p style=\"padding-left: 30px;\">必选：否</p>\n每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。"
      }
    ],
    "desc": "本接口(DescribeReservedInstancesOfferings)供用户列出可购买的预留实例配置"
  },
  "InquiryPriceModifyInstancesChargeType": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "一个或多个待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728)接口返回值中的`InstanceId`获取。每次请求批量实例的上限为100。"
      },
      {
        "name": "InstanceChargeType",
        "desc": "实例[计费类型](https://cloud.tencent.com/document/product/213/2180)。<br><li>PREPAID：预付费，即包年包月。"
      },
      {
        "name": "InstanceChargePrepaid",
        "desc": "预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的续费时长、是否设置自动续费等属性。"
      }
    ],
    "desc": "本接口 (InquiryPriceModifyInstancesChargeType) 用于切换实例的计费模式询价。\n\n* 只支持从 `POSTPAID_BY_HOUR` 计费模式切换为`PREPAID`计费模式。\n* 关机不收费的实例、`BC1`和`BS1`机型族的实例、设置定时销毁的实例、竞价实例不支持该操作。"
  },
  "ModifyDisasterRecoverGroupAttribute": {
    "params": [
      {
        "name": "DisasterRecoverGroupId",
        "desc": "分散置放群组ID，可使用[DescribeDisasterRecoverGroups](https://cloud.tencent.com/document/api/213/17810)接口获取。"
      },
      {
        "name": "Name",
        "desc": "分散置放群组名称，长度1-60个字符，支持中、英文。"
      }
    ],
    "desc": "本接口 (ModifyDisasterRecoverGroupAttribute)用于修改[分散置放群组](https://cloud.tencent.com/document/product/213/15486)属性。"
  },
  "DescribeInternetChargeTypeConfigs": {
    "params": [],
    "desc": "本接口（DescribeInternetChargeTypeConfigs）用于查询网络的计费类型。"
  },
  "RebootInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "一个或多个待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728)接口返回值中的`InstanceId`获取。每次请求批量实例的上限为100。"
      },
      {
        "name": "ForceReboot",
        "desc": "是否在正常重启失败后选择强制重启实例。取值范围：<br><li>TRUE：表示在正常重启失败后进行强制重启<br><li>FALSE：表示在正常重启失败后不进行强制重启<br><br>默认取值：FALSE。"
      },
      {
        "name": "StopType",
        "desc": "关机类型。取值范围：<br><li>SOFT：表示软关机<br><li>HARD：表示硬关机<br><li>SOFT_FIRST：表示优先软关机，失败再执行硬关机<br><br>默认取值：SOFT。"
      }
    ],
    "desc": "本接口 (RebootInstances) 用于重启实例。\n\n* 只有状态为`RUNNING`的实例才可以进行此操作。\n* 接口调用成功时，实例会进入`REBOOTING`状态；重启实例成功时，实例会进入`RUNNING`状态。\n* 支持强制重启。强制重启的效果等同于关闭物理计算机的电源开关再重新启动。强制重启可能会导致数据丢失或文件系统损坏，请仅在服务器不能正常重启时使用。\n* 支持批量操作，每次请求批量实例的上限为100。\n* 实例操作结果可以通过调用 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728#.E7.A4.BA.E4.BE.8B3-.E6.9F.A5.E8.AF.A2.E5.AE.9E.E4.BE.8B.E7.9A.84.E6.9C.80.E6.96.B0.E6.93.8D.E4.BD.9C.E6.83.85.E5.86.B5) 接口查询，如果实例的最新操作状态(LatestOperationState)为“SUCCESS”，则代表操作成功。"
  },
  "DescribeInstanceTypeConfigs": {
    "params": [
      {
        "name": "Filters",
        "desc": "<li><strong>zone</strong></li>\n<p style=\"padding-left: 30px;\">按照【<strong>可用区</strong>】进行过滤。可用区形如：ap-guangzhou-1。</p><p style=\"padding-left: 30px;\">类型：String</p><p style=\"padding-left: 30px;\">必选：否</p><p style=\"padding-left: 30px;\">可选项：<a href=\"https://cloud.tencent.com/document/product/213/6091\">可用区列表</a></p>\n<li><strong>instance-family</strong></li>\n<p style=\"padding-left: 30px;\">按照【<strong>实例机型系列</strong>】进行过滤。实例机型系列形如：S1、I1、M1等。</p><p style=\"padding-left: 30px;\">类型：Integer</p><p style=\"padding-left: 30px;\">必选：否</p>\n每次请求的`Filters`的上限为10，`Filter.Values`的上限为1。"
      }
    ],
    "desc": "本接口 (DescribeInstanceTypeConfigs) 用于查询实例机型配置。\n\n* 可以根据`zone`、`instance-family`来查询实例机型配置。过滤条件详见过滤器[`Filter`](https://cloud.tencent.com/document/api/213/15753#Filter)。\n* 如果参数为空，返回指定地域的所有实例机型配置。"
  },
  "DisassociateSecurityGroups": {
    "params": [
      {
        "name": "SecurityGroupIds",
        "desc": "要解绑的`安全组ID`，类似sg-efil73jd，只支持解绑单个安全组。"
      },
      {
        "name": "InstanceIds",
        "desc": "被解绑的`实例ID`，类似ins-lesecurk，支持指定多个实例 。"
      }
    ],
    "desc": "本接口 (DisassociateSecurityGroups) 用于解绑实例的指定安全组。\n* 实例操作结果可以通过调用 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728#.E7.A4.BA.E4.BE.8B3-.E6.9F.A5.E8.AF.A2.E5.AE.9E.E4.BE.8B.E7.9A.84.E6.9C.80.E6.96.B0.E6.93.8D.E4.BD.9C.E6.83.85.E5.86.B5) 接口查询，如果实例的最新操作状态(LatestOperationState)为“SUCCESS”，则代表操作成功。"
  },
  "AllocateHosts": {
    "params": [
      {
        "name": "Placement",
        "desc": "实例所在的位置。通过该参数可以指定实例所属可用区，所属项目等属性。"
      },
      {
        "name": "ClientToken",
        "desc": "用于保证请求幂等性的字符串。"
      },
      {
        "name": "HostChargePrepaid",
        "desc": "预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。"
      },
      {
        "name": "HostChargeType",
        "desc": "实例计费类型。目前仅支持：PREPAID（预付费，即包年包月模式），默认为：'PREPAID'。"
      },
      {
        "name": "HostType",
        "desc": "CDH实例机型，默认为：'HS1'。"
      },
      {
        "name": "HostCount",
        "desc": "购买CDH实例数量，默认为：1。"
      },
      {
        "name": "TagSpecification",
        "desc": "标签描述列表。通过指定该参数可以同时绑定标签到相应的资源实例。"
      }
    ],
    "desc": "本接口 (AllocateHosts) 用于创建一个或多个指定配置的CDH实例。\n* 当HostChargeType为PREPAID时，必须指定HostChargePrepaid参数。"
  },
  "DescribeHosts": {
    "params": [
      {
        "name": "Filters",
        "desc": "<li><strong>zone</strong></li>\n<p style=\"padding-left: 30px;\">按照【<strong>可用区</strong>】进行过滤。可用区形如：ap-guangzhou-1。</p><p style=\"padding-left: 30px;\">类型：String</p><p style=\"padding-left: 30px;\">必选：否</p><p style=\"padding-left: 30px;\">可选项：<a href=\"https://cloud.tencent.com/document/product/213/6091\">可用区列表</a></p>\n<li><strong>project-id</strong></li>\n<p style=\"padding-left: 30px;\">按照【<strong>项目ID</strong>】进行过滤，可通过调用[DescribeProject](https://cloud.tencent.com/document/api/378/4400)查询已创建的项目列表或登录[控制台](https://console.cloud.tencent.com/cvm/index)进行查看；也可以调用[AddProject](https://cloud.tencent.com/document/api/378/4398)创建新的项目。项目ID形如：1002189。</p><p style=\"padding-left: 30px;\">类型：Integer</p><p style=\"padding-left: 30px;\">必选：否</p>\n<li><strong>host-id</strong></li>\n<p style=\"padding-left: 30px;\">按照【<strong>[CDH](https://cloud.tencent.com/document/product/416) ID</strong>】进行过滤。[CDH](https://cloud.tencent.com/document/product/416) ID形如：host-xxxxxxxx。</p><p style=\"padding-left: 30px;\">类型：String</p><p style=\"padding-left: 30px;\">必选：否</p>\n<li><strong>host-name</strong></li>\n<p style=\"padding-left: 30px;\">按照【<strong>CDH实例名称</strong>】进行过滤。</p><p style=\"padding-left: 30px;\">类型：String</p><p style=\"padding-left: 30px;\">必选：否</p>\n<li><strong>host-state</strong></li>\n<p style=\"padding-left: 30px;\">按照【<strong>CDH实例状态</strong>】进行过滤。（PENDING：创建中 | LAUNCH_FAILURE：创建失败 | RUNNING：运行中 | EXPIRED：已过期）</p><p style=\"padding-left: 30px;\">类型：String</p><p style=\"padding-left: 30px;\">必选：否</p>\n每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。"
      }
    ],
    "desc": "本接口 (DescribeHosts) 用于获取一个或多个CDH实例的详细信息。"
  }
}