import os

import sys

class main:

    def services_exist(self):

        projects = os.getenv("Project_id")

        projects_list = projects.split(",")
        
        project_not_deleted = False

        for projects in projects_list:

            project_id = projects

            print("Checking whether services existed or not in project" + project_id)

            from gcp_project_deletion.compute import compute

            obj_compute = compute()

            instance_exist = obj_compute.vm_list(project_id)

            from gcp_project_deletion.disks import disks

            obj_disks = disks()

            disks_exist = obj_disks.disks_list(project_id)

            from gcp_project_deletion.firewall import firewall

            obj_firewall = firewall()

            firewall_exist = obj_firewall.firewall_list(project_id)

            from gcp_project_deletion.vpn import vpn

            obj_vpn = vpn()

            vpn_exist = obj_vpn.vpn_list(project_id)

            from gcp_project_deletion.storage import storage

            obj_storage = storage()

            storage_exist = obj_storage.storage_list(project_id)

            from gcp_project_deletion.liens import liens

            obj_liens = liens()

            liens_exist = obj_liens.liens_list(project_id)

            if (instance_exist | disks_exist | firewall_exist | vpn_exist | liens_exist):

                print("Project " + project_id + " will not  be deleted")
                
                project_not_deleted = True

            else:
                
                from gcp_project_deletion.endpoint import endpoint

                obj_endpoint = endpoint()

                endpoint_exist = obj_endpoint.endpoint_list(project_id)

                from gcp_project_deletion.variable import resource_manager_service

                request = resource_manager_service.projects().delete(projectId=project_id)

                request.execute()

                print("Project " + project_id + " is now shutdown")
                
        if project_not_deleted == True:

                sys.exit(-1)

        else:
                print("All projects got deleted")

obj_main = main()

obj_main.services_exist()
