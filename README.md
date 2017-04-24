## How to use:

Running the container as default configures a local SQLite database:
`docker run -d -p 80:5000 chris24walsh/flask-aws:latest`

If you want to use a remote MYSQL database, pass these command arguments at runtime:
`(...-aws:latest) /bin/sh set_db_URI.sh /
"mysql+pymysql://<db_username<db_password>@<db_endpoint>:3306/<db_name>'"`

###
###

## How to set up a load balanced and redundant Flask WebApp on ECS with Docker 

### 1 Configure the ECS cluster

Sign in to AWS. You will need a verified account.

##### 1.1 Create ECS cluster

Navigate to the EC2 Container Services (ECS) service. Create a new cluster. Tick the "Create an empty cluster" checkbox and click 'Create'. Thats it for now.

##### 1.2 Setup load balancer

From the 'Services' menu, choose the EC2 console. Scroll down on the left hand menu and select 'Load Balancers'. Create a new load balancer - we chose the 'Classic Load Balancer' for no particular reason. 

In Step 1 of the wizard, we chose a name and went with the default options. In Step 2, we configured a new security group which allowed traffic on port 80. We are going to ignore the need for a Secure Listener (SSL terminator) in step 3. In step 4, configure the ping path to '/', as that's all docker can handle. Skip adding EC2 instances for now. Skip adding tags and review and create your load balancer. 

##### 1.3 Configure roles for EC2, ECS and ELB communication

Before creating an auto-scaling group, you will need a couple of appropriate IAM roles to be created.

Firstly, by default your EC2 instances do not have permissions to talk to an ECS cluster, you need to create a role to support this. This role will be attached to your EC2 instances when we create them. From the IAM services console, choose an 'Amazon EC2' AWS Service Role. You will need to attach the 'AmazonEC2ContainerServiceforEC2Role' policy for your new role.

Secondly, you need a role to allow the ECS cluster to talk to your ELB. From the 'AWS Service Roles' select 'Amazon EC2 Container Service Role' and attach the 'AmazonEC2ContainerServiceRole' policy to your role.

##### 1.4 Setup an auto-scaling group

From the EC2 console, scroll down to 'Auto Scaling Groups'. Create an auto-scaling group and create a launch configuration. Choose an AMI from the AWS Marketplace - 'Amazon ECS-Optimised Amazon Linux AMI'. We chose General Purpose t2.micro. Set the name of your launch configuration and assign the IAM role you created for allowing your EC2 instances to talk to your ECS cluster.

From Advanced Details drop down menu, add the following bash script to the User Data section:

```
#!/bin/bash

echo ECS_CLUSTER=flask-test-ecs-cluster > /etc/ecs/ecs.config
```

Next, accept the default EBS volume for storage and proceed to creating a security group. Create a new security group with a HTTP rule which allows traffic from anywhere. Create the launch configuration and proceed without a keypair as the instance will only need to host a docker image.

Now, create your auto scaling group with the default VPC and any of the default subnets.

For now, keep the auto scaling group at its initial size, ignore notifications and tags.


### 2 Create and Dockerise WebApp 

(tbc)

### 3 Publish Webapp to ECS cluster

(tbc)
