# Wordpress Cloudformation

Hi! This is my template for the test. The request was as follow:

"**Excercise 4**
Quick! A new WordPress site must go live!
You have these instructions: 
- Automate the creation of the infrastructure and the setup of the application
- It's based on the last version of WordPress (it will be more useful if we can parameterize the version) 
- You can choose Apache, Nginx, or whatever you want. 
- Once deployed, the application should be:  secure , fast , fault-tolerant , adaptive to average load 
- To provision the infrastructure, choose one between CloudFormation and Terraform (CloudFormation, Terraform) 
- Optional: Create a CI/CD pipeline to deploy WordPress 
- Write a readme with an architecture diagram and all the required instructions to install and try your solution

## Diagram

![diagram](https://github.com/mbeccalli/cloudformation_wordpress_exercise/blob/main/Diagram.png)

I started from [the sample template](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/sample-templates-applications-eu-west-1.html) from AWS and loosely based my architecture on [Wordpress best practices on AWS](https://aws.amazon.com/blogs/architecture/wordpress-best-practices-on-aws/).

Regarding some particular bits from the template:
- to get the default route table and attach the internet gateway to it when I created the VPC, I used the script that can be [found here](https://repost.aws/knowledge-center/cloudformation-route-table-vpc) shared by the AWS team. 
- I didn't have time to refactor it as a nested stack, I would have split every logical bit into a different stack. 


## How to run

To run the template, log in into AWS console and go to Cloudformation. Upload the template "CF_Wordpress.yaml" and run it.

The parameters requested are:
- Wordpress DB Name
- Wordpress DB User
- Wordpress DB User password
- Wordpress Installation version
- Server Istance Type
- VPC CIDR Block
- Public Subnet 1 CIDR Block
- Public Subnet 2 CIDR Block
- SSH Location CIDR Block

Once installed, one of the outputs is the loadbalancer entry point and the other the CloudFront Distribution URL. Having an SSL certificate and a domain name, it would be possible to add it to Route53, register it as an alias on CloudFront and run the distribution as the website.
