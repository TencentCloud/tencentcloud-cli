# 命令行工具简介
欢迎使用腾讯云命令行工具(TCCLI)，TCCLI是管理腾讯云资源的统一工具。通过腾讯云命令行工具，您可以快速轻松的调用腾讯云 API来管理您的腾讯云资源。您还可以基于腾讯云的命令行工具来做自动化和脚本处理，能够以更多样的方式进行组合和重用。
# 安装TCCLI
1. 安装 Python 环境和 Pip 工具，安装命令行工具前请确保您的系统已经安装了 Python 环境和 Pip 工具。**注意python版本必须为2.7及以上版本**,更多内容请参考[python主页](https://www.python.org/)和[pip主页](https://pypi.org/project/pip/)。
2. TCCLI依赖于TencentCloudApi Python SDK，**如果TencentCloudApi Python SDK的版本号小于要安装TCCLI版本号，在安装TCCLI时会自动升级TencentCloudApi Python SDK**。
3. 安装TCCLI，执行以下命令：
```bash
pip install tccli
```
如果是MacOS用户，您还可以使用homebrew来安装tccli：

> 执行如下命令之前您需要先安装homebrew，安装的方法可以参考[homebrew官网](https://brew.sh/index_zh-cn)
```bash
brew tap tencentcloud/tccli
brew install tccli
```
注意：如果是从3.0.252.3以下版本升级的需要执行
```bash
sudo pip uninstall tccli jmespath
sudo pip install tccli
```
4. 安装完成之后执行tccli --version检测是否安装成功。
5. 如果您的环境是linux环境，您可以通过以下命令启动自动补全功能：
```bash
complete -C 'tccli_completer' tccli
```
可以将命令``complete -C 'tccli_completer' tccli``加入环境变量(/etc/profile)中，使自动补全功能一直有效。

## 在 Docker 上使用

```shell
docker run --rm -it tencentcom/tencentcloud-cli --version
docker run --rm -it tencentcom/tencentcloud-cli help
```

## 在 Coding-CI 上使用

```yaml
master:
  push:
  - stages:
    - name: run with tencentcloud-cli
      image: tencentcom/tencentcloud-cli
      commands: |
        tccli --version
        tccli help
```        

# 配置TCCLI
要使用腾讯云命令行工具，您还需要进行一些初始化配置，使其完成使用 云 API的必要前提条件。
1. 交互模式，您可以通过tccli configure命令进入交互模式快速配置。

```bash
$  tccli configure
TencentCloud API secretId [*afcQ]:AKIDwLw1234MMfPRle2g9nR2OTI787aBCDP
TencentCloud API secretKey [*ArFd]:OxXj7khcV1234dQSSYNABcdCc1LiArFd
region: ap-guangzhou
output[json]:
```
secretId: 云 API 密钥SecretId。
secretIKey: 云 API 密钥SecretKey。
region： 云产品地域，请移驾对应产品页面获取可用的region。
output： 可选参数，请求回包输出格式，支持[json table text]三种格式，默认为json。
更多信息请执行tccli configure help查看。

注意：如果环境变量定义了相关配置，则会优先于配置文件生效。分别为 TENCENTCLOUD\_SECRET\_ID，TENCENTCLOUD\_SECRET\_KEY，TENCENTCLOUD\_REGION。

2. 命令行模式，通过命令行模式您可以在自动化脚本中配置您的信息。
```bash
# set子命令可以设置某一配置，也可同时配置多个。
tccli configure set secretId AKIDwLw1234MMfPRle2g9nR2OTI787aBCDP
tccli configure set region ap-guangzhou  output json language zh-CN

# get子命令用于获取配置信息。
tccli configure get secretKey
secretKey = OxXj7khcV1234dQSSYNABcdCc1LiArFd

# list子命令打印所有配置信息。
tccli configure list
credential:
secretId =  AKIDwLw1234MMfPRle2g9nR2OTI787aBCDP
secretKey =  OxXj7khcV1234dQSSYNABcdCc1LiArFd
configure:
region =  ap-guangzhou
output =  json
language = zh-CN

# remove子命令删除配置文件
tccli configure remove
```
更多信息请执行tccli configure [list get set remove] help查看。

3. 多账户支持，TCCLI支持多账户，方便您多种配置同时使用。
```bash
在交互模式中指定账户名test。
$  tccli configure --profile test
TencentCloud API secretId [*BCDP]:AKIDwLw1234MMfPRle2g9nR2OTI787aBCDP
TencentCloud API secretKey [*ArFd]:OxXj7khcV1234dQSSYNABcdCc1LiArFd
region: ap-guangzhou
output[json]:

# set/get/list/remove子命令指定账户名test。
tccli configure set region ap-guangzhou  output json language zh-CN --profile test
tccli configure get secretKey      --profile test
tccli configure list      --profile test
tccli configure remove      --profile test


在调用接口时指定账户(以cvm DescribeZones接口为例)。
tccli cvm DescribeZones --profile test
```
如果不希望输入命令是手动指定账户名，还可以设置环境变量，tccli能从环境变量中读取指定的profile
```bash
export TCCLI_PROFILE=test
```

4. 您可以配置https代理，让tccli通过代理调用API

在环境变量中配置https代理
```bash
# 在Linux/Unix和macOS中执行如下类似命令配置环境变量
export https_proxy=https://192.168.1.1:1111
export https_proxy=https://myproxy.com:1111

# 在Windows的终端中执行如下类似命令配置环境变量
setx http_proxy=https://192.168.1.1:1111
set  http_proxy=https://myproxy.com:1111
# setx表示设置永久环境变量，设置后重启终端生效
```

您也可以直接使用'--https-proxy'选项设置https代理
```bash
# 例如
tccli cvm DescribeRegions --https-proxy https://192.168.1.1:1111
```

# 凭证管理

腾讯云命令行工具（TCCLI）目前支持以下几种方式进行凭证管理，获取凭证的优先级：实例角色 > 角色 > TKE OIDC > 临时密钥 > 永久密钥：

1. 实例角色

有关实例角色的相关概念请参阅：[腾讯云实例角色](https://cloud.tencent.com/document/product/213/47668)

在您为实例绑定角色后，您可以在实例中访问相关元数据接口获取临时凭证，SDK 会自动刷新临时凭证。相关命令如下：

使用方式：
- 命令行输入
```bash
tccli cvm DescribeRegions --use-cvm-role
```

2. 角色

有关角色的相关概念请参阅：[腾讯云角色概述](https://cloud.tencent.com/document/product/598/19420)

要使用此种方式，您必须在腾讯云访问管理控制台上创建了一个角色，具体创建过程请参阅：[腾讯云角色创建](https://cloud.tencent.com/document/product/598/19381)

在您拥有角色后，可以通过如下方式获取临时凭证，相关命令如下：

- 命令行输入

```bash
tccli cvm DescribeRegions --secretId xx --secretKey xx --role-arn xx --role-session-name
```

- 环境变量

配置环境变量：`TENCENTCLOUD_SECRET_ID`, `TENCENTCLOUD_SECRET_KEY`, `TENCENTCLOUD_ROLE_ARN`, `TENCENTCLOUD_ROLE_SESSION_NAME`

3. TKE OIDC

- 环境变量
  配置环境变量：`TKE_REGION`, `TKE_PROVIDER_ID`, `TKE_WEB_IDENTITY_TOKEN_FILE`, `TKE_ROLE_ARN`

4. 临时密钥

- 命令行输入
```bash
tccli cvm DescribeRegions --secretId xx --secretKey xx --token xx
```


- 环境变量
  配置环境变量：`TENCENTCLOUD_SECRET_ID`, `TENCENTCLOUD_SECRET_KEY`, `TENCENTCLOUD_TOKEN`


- xxx.credential文件
```json
{
  "secretId": "AKIDxxxxxxxxxxxxxxxxxxxxQsPk",
  "secretKey": "QgoxxxxxxxxxxxxxxxxgvW4",
  "token": "xxxxxxxxxxxxxxxxxx"
}
```


5. 永久密钥

- 命令行输入
```bash
tccli cvm DescribeRegions --secretId xx --secretKey xx
```


- 环境变量
  配置环境变量：`TENCENTCLOUD_SECRET_ID`, `TENCENTCLOUD_SECRET_KEY`


- xxx.credential文件
```json
{
  "secretId": "AKIDxxxxxxxxxxxxxxxxxxxxQsPk",
  "secretKey": "QgoxxxxxxxxxxxxxxxxgvW4"
}
```

# 使用TCCLI
命令行工具集成了腾讯云所有支持云 API 的产品，可以在命令行下完成对腾讯云产品的配置和管理。包括使用TCCLI创建云服务器，操作云服务器，通过TCCLI创建CBS盘、查看CBS盘使用情况，通过TCCLI创建VPC网络、往VPC网络中添加资源等等，所有在控制台页面能完成的操作，均能再命令行工具上执行命令实现。
* 通过tccli cvm DescribeInstances命令查看当前账号有哪些云服务器。
* 通过tccli cbs DescribeDisks命令查看有CBS盘列表。

以创建一台cvm为例(**请注意demo中非简单类型的参数必须为标准json格式**)：
```bash
tccli cvm RunInstances --InstanceChargeType POSTPAID_BY_HOUR --InstanceChargePrepaid '{"Period":1,"RenewFlag":"DISABLE_NOTIFY_AND_MANUAL_RENEW"}'
 --Placement '{"Zone":"ap-guangzhou-2"}' --InstanceType S1.SMALL1 --ImageId img-8toqc6s3 --SystemDisk '{"DiskType":"CLOUD_BASIC", "DiskSize":50}'
--InternetAccessible '{"InternetChargeType":"TRAFFIC_POSTPAID_BY_HOUR","InternetMaxBandwidthOut":10,"PublicIpAssigned":true}' --InstanceCount 1
--InstanceName TCCLI-TEST --LoginSettings '{"Password":"isd@cloud"}' --SecurityGroupIds '["sg-0rszg2vb"]' --HostName TCCLI-HOST-NAME1
```
更多功能，您可以通过tccli help查看支持的产品，通过tccli cvm help（以cvm举例）查看产品支持的接口。通过tccli cbs DescribeDisks help(以cbs产品的DescribeDisks接口为例) 查看接口支持的参数。如果想看详细信息，可以在help的后面增加字段'--detail'查看。例如：分别使用tccli help --detail，tccli cvm help --detail和tccli cbs DescribeDisks help --detail查看对应的详细信息。

# 高级功能
## 多版本接口访问
某些产品可能存在多个版本的接口，TCCLI默认访问最新版本的接口。如果您想访问特定旧版本的接口，可以通过以下方式实现(以cvm举例)。
```bash
# 设置cvm产品默认使用版本:2017-03-12。
tccli configure set cvm.version 2017-03-12

# 在实时使用时指定版本号。
tccli cvm help --version 2017-03-12
tccli cvm DescribeZones help --version 2017-03-12
tccli cvm DescribeZones --version 2017-03-12
```
## 指定输出语言
指定公共参数`language`可以获得接口指定语言的返回，`language`参数也支持在配置文件中配置，默认值为"zh-CN"
```
# 在实时使用时指定语言
tccli cvm DescribeZones --language zh-CN
tccli cvm DescribeZones --language en-US
```
## 指定最近的接入点(Endpoint)
TCCLI默认会请求就近的接口点访问服务，你也可以针对某一产品指定自己的Endpoint(以cvm为例)。
```bash
# 设置cvm产品默认endpoint。
tccli configure set cvm.endpoint cvm.ap-guangzhou.tencentcloudapi.com

# 调用时实时指定。
tccli cvm DescribeZones --endpoint cvm.ap-guangzhou.tencentcloudapi.com
```
## 返回结果过滤

TCCLI 支持 [JMESPath](https://jmespath.org/examples.html) ，以下仅为部分示例，全部过滤能力请参考 JMESPath 官方文档。

1. 不加任何过滤时的输出(以cvm DescribeZones接口的返回为例)。
```bash
[root@VM_180_248_centos ~]# tccli cvm DescribeZones
{
    "TotalCount": 4,
    "ZoneSet": [
        {
            "ZoneState": "AVAILABLE",
            "ZoneId": "100001",
            "Zone": "ap-guangzhou-1",
            "ZoneName": "广州一区"
        },
        {
            "ZoneState": "AVAILABLE",
            "ZoneId": "100002",
            "Zone": "ap-guangzhou-2",
            "ZoneName": "广州二区"
        },
        {
            "ZoneState": "AVAILABLE",
            "ZoneId": "100003",
            "Zone": "ap-guangzhou-3",
            "ZoneName": "广州三区"
        },
        {
            "ZoneState": "AVAILABLE",
            "ZoneId": "100004",
            "Zone": "ap-guangzhou-4",
            "ZoneName": "广州四区"
        }
    ],
    "RequestId": "4fd313a6-155f-4c7a-bf86-898c02fcae02"
}
```
2. 只看某个字段。
```bash
[root@VM_180_248_centos ~]# tccli cvm DescribeZones  --filter TotalCount
4
```
3. 指定某个数组类型对象的第N个子对象的信息。
注意：Mac OS 系统使用如下命令可能会报错 `zsh: no matches found: xxx`，这时需要将说明过滤行为的内容用单引号包裹起来
```bash
[root@VM_180_248_centos ~]# tccli cvm DescribeZones  --filter ZoneSet[0]
{
    "ZoneState": "AVAILABLE",
    "ZoneId": "100001",
    "Zone": "ap-guangzhou-1",
    "ZoneName": "广州一区"
}
```
4. 指定数组类型对象下所有某个名称的子对象的某个字段。
```bash
[root@VM_180_248_centos ~]# tccli cvm DescribeZones  --filter ZoneSet[*].ZoneName
[
    "广州一区",
    "广州二区",
    "广州三区",
    "广州四区"
]
```
5. 过滤数组里的子对象，同时还以新的名称展示。
注意：这里需要将说明过滤行为的内容用单引号包裹起来。
```bash
[root@VM_180_248_centos ~]# tccli cvm DescribeZones  --filter 'ZoneSet[*].{name:ZoneName, id:ZoneId}'
[
    {
        "name": "广州一区",
        "id": "100001"
    },
    {
        "name": "广州二区",
        "id": "100002"
    },
    {
        "name": "广州三区",
        "id": "100003"
    },
    {
        "name": "广州四区",
        "id": "100004"
    }
]
```
6. 高级过滤。CVM 的 DescribeInstances 接口，返回结构体中 InstanceSet 是一个数组，里面每个元素都是一个实例的信息。假设我们想要获取中国香港地域每个实例的唯一标识符 InstanceId，实例名称 InstanceName，并且过滤特定标签。标签是一个数组，里面每个元素是一个字典，键值 Key 是标签名，键值 Value 是标签值，我们想要获取标签名是`app`的标签值。最后结果打印文本。注意，过滤的标签值实际为数组，我们只取第一个，确保不会因为是数组而导致换行。此外，复杂的命令行语句编写困难，维护不便，建议使用 SDK 封装为程序调用更为合理。
```
tccli cvm DescribeInstances --region ap-hongkong --filter 'InstanceSet[].[InstanceId,InstanceName,Tags[?Key==`app`].Value|[0]]' --output text
ins-6xe51ktg    未命名  elastic-search
```
## 结果轮询
可以使用'--waiter'参数来轮询实例的信息直到出现指定的状态
```
# 例如执行如下命令，程序将一定的时间间隔对实例的状态进行轮询，直到实例的状态为'RUNNING'或者超时为止，`--region`的值需改为您的实例所在的地域
tccli cvm DescribeInstancesStatus --region ap-hongkong --waiter "{'expr':'InstanceStatusSet[0].InstanceState','to':'RUNNING'}"
# 您可以自己指定超时的时间和睡眠的时间，如下面的例子，设定的超时时间为180秒，睡眠的时间为5秒。
tccli cvm DescribeInstancesStatus --region ap-hongkong --waiter "{'expr':'InstanceStatusSet[0].InstanceState','to':'RUNNING','timeout':180,'interval':5}"
```
使用'--waiter'参数时，必须指定一以下两个参数：

- expr: 指定被查询的字段，使用[jmespath](http://jmespath.org/)来查找被指定的字段的值
- to: 被轮询的字段的目标值

可选子参数：

- timeout: 轮询的超时时间(s)
- inaterval: 进程睡眠的时间(s)

您可以在配置文件中设置可选子参数的值，例如
```
# 在default.configure文件中，您可以添加如下参数，设置系统超时时间为180诗，睡眠时间为5s
    "waiter": {
        "interval": 5,
        "timeout": 180
      },
```
## 输出入参骨架到json文件
```bash
[root@VM_180_248_centos ~]# tccli cvm RunInstances  --generate-cli-skeleton > /tmp/RunInstances.json
```
## 从json文件读取参数，--cli-input-json后接file://+文件路径
```bash
[root@VM_180_248_centos ~]# tccli cvm RunInstances --cli-input-json file:///tmp/RunInstances.json
{
    "RequestId": "20e2b42d-3260-4750-9293-79116208330e", 
    "InstanceIdSet": null
}
```
