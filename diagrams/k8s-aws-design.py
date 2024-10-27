from diagrams import Diagram, Cluster, Edge
from diagrams.aws.network import VPC, PublicSubnet, PrivateSubnet, NATGateway, InternetGateway
from diagrams.aws.database import RDS
from diagrams.aws.compute import EKS
from diagrams.k8s.compute import Pod
from diagrams.k8s.controlplane import API
from diagrams.k8s.network import Ingress, Service
from diagrams.onprem.monitoring import Prometheus, Grafana

with Diagram("Modern Kubernetes on AWS with Grafana Monitoring", direction="TB"):
    # AWS Infrastructure
    with Cluster("AWS Cloud"):
        vpc = VPC("VPC")

        igw = InternetGateway("Internet Gateway")
        nat_gw = NATGateway("NAT Gateway")

        with Cluster("Public Subnet"):
            public_subnet = PublicSubnet("Public Subnet")
            grafana = Grafana("Grafana")
            nlb = Service("Network Load Balancer")

        with Cluster("Private Subnet"):
            private_subnet = PrivateSubnet("Private Subnet")
            rds = RDS("Database")

            with Cluster("Kubernetes Cluster"):
                eks = EKS("EKS Cluster")
                with Cluster("Node Group"):
                    app_pod = Pod("App Pod")
                    ingress = Ingress("Ingress Controller")
                    prometheus = Prometheus("Prometheus")

                    # Application Pod and Services
                    app_pod - Edge(label="Metrics") - prometheus
                    prometheus >> Edge(label="Metrics") >> grafana

        # Networking Connections
        vpc >> igw
        vpc >> public_subnet >> nlb >> ingress >> eks
        eks >> private_subnet

