#  Command Line Tool Introduction
Welcome to Tencent Cloud Command Line Tool (TCCLI), a unified tool for managing Tencent cloud resources. With Tencent Cloud Command Line Tools, you can quickly and easily call the Tencent Cloud API to manage your Tencent cloud resources. You can also automate and script based on Tencent Cloud's command-line tools, which can be combined and reused in a variety of ways.
# Install TCCLI
1. Install the Python environment and Pip tools. Before installing the command line tools, make sure your system has the Python environment and Pip tools installed. **Note that the python version must be 2.7 and above**, please refer to [python homepage](https://www.python.org/) and [pip homepage](https://pypi.org/project/pip/).
2. TCCLI relies on the TencentCloudApi Python SDK. **If the version number of the TencentCloudApi Python SDK is smaller than the TCCLI version number to be installed, the TencentCloudApi Python SDK will be automatically upgraded when TCCLI is installed.** 
3. Install TCCLI and execute the following command:
```bash
pip install tccli
```
4. After the installation is complete, execute tccli version to check whether the installation is successful.
5. If your environment is a Linux environment, you can enable auto-completion with the following command:
```bash
complete -C 'tccli_completer' tccli
```

# Configure TCCLI
To use the Tencent Cloud Command Line tool, you also need to do some initial configuration to make it necessary to use the Cloud API.
1. Interactive mode, you can use the tccli configure command to enter interactive mode for quick configuration.

```bash
$ tccli configure
TencentCloud API secretId [*afcQ]: AKIDwLw1234MMfPRle2g9nR2OTI787aBCDP
TencentCloud API secretKey [*ArFd]:OxXj7khcV1234dQSSYNABcdCc1LiArFd
region: ap-guangzhou
output[json]:
```
secretId: Cloud API key SecretId.
secretIKey: Cloud API key SecretKey.
Region: Cloud product area, please go to the corresponding product page to get the available region.
Output: Optional parameter, request return packet output format, support [json table text] three formats, the default is json.
For more information, please see tccli configure help.

2. Command line mode, you can configure your information in an automation script via command line mode.
```bash
The #set subcommand can set a certain configuration or configure multiple at the same time.
tccli configure set secretId AKIDwLw1234MMfPRle2g9nR2OTI787aBCDP
tccli configure set region ap-guangzhou output json

# The get subcommand is used to obtain configuration information.
tccli configure get secretKey
secretKey = OxXj7khcV1234dQSSYNABcdCc1LiArFd

# list subcommand prints all configuration information.
tccli configure list
credential:
secretId = AKIDwLw1234MMfPRle2g9nR2OTI787aBCDP
secretKey = OxXj7khcV1234dQSSYNABcdCc1LiArFd
configure:
region = ap-guangzhou
output = json
```
For more information, please run tccli configure [list get set] help.

3. Multi-account support, TCCLI supports multiple accounts, which is convenient for you to use multiple configurations at the same time.
```bash
Specify the account name test in interactive mode.
$ tccli configure --profile test
TencentCloud API secretId [*BCDP]: AKIDwLw1234MMfPRle2g9nR2OTI787aBCDP
TencentCloud API secretKey [*ArFd]:OxXj7khcV1234dQSSYNABcdCc1LiArFd
region: ap-guangzhou
output[json]:

The #set/get/list subcommand specifies the account name test.
tccli configure set region ap-guangzhou output json --profile test
tccli configure get secretKey --profile test
tccli configure list --profile test


Specify the account when calling the interface (take the cvm DescribeZones interface as an example).
tccli cvm DescribeZones --profile test
```


# Using TCCLI
The command line tool integrates all Tencent Cloud products that support the Cloud API. You can configure and manage Tencent cloud products from the command line. This includes creating a cloud server using TCCLI, operating a cloud server, creating a CBS disk through TCCLI, viewing the usage of the CBS disk, creating a VPC network through TCCLI, adding resources to the VPC network, etc. All operations that can be done on the console page can be performed. Then execute the command on the command line tool.
* Use the tccli cvm DescribeInstances command to view which cloud servers are currently on the account.
* View the list of CBS disks by using the tccli cbs DescribeDisks command.

Take the example of creating a cvm (**Please note that the non-simple type of parameters in the demo must be in the standard json format**):
```bash
tccli cvm RunInstances --InstanceChargeType POSTPAID_BY_HOUR --InstanceChargePrepaid '{"Period":1,"RenewFlag":"DISABLE_NOTIFY_AND_MANUAL_RENEW"}'
 --Placement '{"Zone":"ap-guangzhou-2"}' --InstanceType S1.SMALL1 --ImageId img-8toqc6s3 --SystemDisk '{"DiskType":"CLOUD_BASIC", "DiskSize":50}'
--InternetAccessible '{"InternetChargeType":"TRAFFIC_POSTPAID_BY_HOUR","InternetMaxBandwidthOut":10,"PublicIpAssigned":true}' --InstanceCount 1
--InstanceName TCCLI-TEST --LoginSettings '{"Password":"isd@cloud"}' --SecurityGroupIds '["sg-0rszg2vb"]' --HostName TCCLI-HOST-NAME1
```
For more features, you can check out the supported products with tccli help and check the supported interfaces with tccli cvm help (example cvm). Use the tccli cbs DescribeDisks help (using the DescribeDisks interface of the cbs product as an example) to view the parameters supported by the interface.

# Advanced Features
## Multi-version interface access
Some products may have multiple versions of the interface, and TCCLI accesses the latest version of the interface by default. If you want to access a specific old version of the interface, you can do so in the following way (in cvm example).
```bash
# Set the default version of the cvm product: 2017-03-12.
tccli configure set cvm.version 2017-03-12

# Specify the version number when using it in real time.
tccli cvm help --version 2017-03-12
tccli cvm DescribeZones help --version 2017-03-12
tccli cvm DescribeZones --version 2017-03-12
```
## Specify the nearest access point (Endpoint)
By default, TCCLI requests the nearest interface point to access the service. You can also specify your own Endpoint for a product (using cvm as an example).
```bash
# Set the default endpoint of the cvm product.
tccli configure set cvm.endpoint cvm.ap-guangzhou.tencentcloudapi.com

# Specify in real time when called.
tccli cvm DescribeZones --endpoint cvm.ap-guangzhou.tencentcloudapi.com
```
## Return result filtering
1. Output without any filtering (take the return of the cvm DescribeZones interface as an example).
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
2. Just look at a field.
```bash
[root@VM_180_248_centos ~]# tccli cvm DescribeZones --filter TotalCount
4
```
3. Specify information for the Nth child of an array type object.
```bash
[root@VM_180_248_centos ~]# tccli cvm DescribeZones --filter ZoneSet[0]
{
    "ZoneState": "AVAILABLE",
    "ZoneId": "100001",
    "Zone": "ap-guangzhou-1",
    "ZoneName": "广州一区"
}
```
4. Specify a field of a sub-object of all the names under the array type object.
```bash
[root@VM_180_248_centos ~]# tccli cvm DescribeZones --filter ZoneSet[*].ZoneName
[
    "广州一区",
    "广州二区",
    "广州三区",
    "广州四区"
]
```
5. Filter the child objects in the array and also present them under the new name.
Note: The content that describes the filtering behavior needs to be wrapped in single quotes.
```bash
[root@VM_180_248_centos ~]# tccli cvm DescribeZones --filter 'ZoneSet[*].{name:ZoneName, id:ZoneId}'
[
    {
        "name": "Guangzhou District",
        "id": "100001"
    },
    {
        "name": "Guangzhou Second District",
        "id": "100002"
    },
    {
        "name": "Guangzhou three districts",
        "id": "100003"
    },
    {
        "name": "Guangzhou Four Districts",
        "id": "100004"
    }
]
```

