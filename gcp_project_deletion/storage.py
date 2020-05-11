class storage:

    def storage_list(self,project_id):

        storage_exist = False

        from gcp_project_deletion.variable import storage_client

        buckets = list(storage_client.list_buckets(project=project_id))

        if len(buckets)>0:

            print("Buckets exists in project please delete")

            storage_exist = True

        else:

            print("Buckets doesn't exists in the project")

        return storage_exist



