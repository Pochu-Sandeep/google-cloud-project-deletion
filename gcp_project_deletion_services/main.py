import os

import sys

class main:

    def services_exist(self):

        projects = input("Enter project id : ")

        projects_list = projects.split(",")

        for projects in projects_list:

                project_id = projects

                print("Checking for VM's,Firewalls,VPN,Storage,Liens and Endpoints in project " + project_id)

                from gcp_project_deletion_services.compute import compute

                obj_compute = compute()

                instance_exist = obj_compute.vm_list(project_id)

                from gcp_project_deletion_services.firewall import firewall

                obj_firewall = firewall()

                firewall_exist = obj_firewall.firewall_list(project_id)

                from gcp_project_deletion_services.vpn import vpn

                obj_vpn = vpn()

                vpn_exist = obj_vpn.vpn_list(project_id)

                from gcp_project_deletion_services.storage import storage

                obj_storage = storage()

                storage_exist = obj_storage.storage_list(project_id)

                from gcp_project_deletion_services.liens import liens

                obj_liens = liens()

                liens_exist = obj_liens.liens_list(project_id)

                from gcp_project_deletion_services.endpoint import endpoint

                obj_endpoint = endpoint()

                endpoint_exist = obj_endpoint.endpoint_list(project_id)

                if (instance_exist | firewall_exist | vpn_exist | storage_exist | liens_exist | endpoint_exist):

                        print("Project "+project_id+" will not  be deleted")

                else:

                        from gcp_project_deletion_services.variable import resource_manager_service

                        request = resource_manager_service.projects().delete(projectId=project_id)

                        request.execute()

                        print("Project "+project_id+" is now shutdown")

        for projects in projects_list:

                project_id = projects

                from gcp_project_deletion_services.variable import resource_manager_service

                project_status_request = resource_manager_service.projects().get(projectId=project_id)

                project_status_response = project_status_request.execute()

                project_status = project_status_response.get('lifecycleState')

                if project_status == 'ACTIVE':

                        print(project_id+" is not deleted")

                else:

                        print(project_id+" is deleted")

obj_main = main()

obj_main.services_exist()