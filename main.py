
from diagrams import Diagram, Cluster
from diagrams.aws.network import VPC, PublicSubnet, InternetGateway
from diagrams.aws.compute import EC2

with Diagram("AWS構成図", show=False):
    igw = InternetGateway("Internet Gateway")
    with Cluster('VPC'):

        vpc = VPC("VPC")
        pub_subnet = PublicSubnet("Public Subnet")

        with Cluster("Public Subnet"):
            ec2 = EC2("EC2")

    igw >> vpc >> pub_subnet >> ec2


