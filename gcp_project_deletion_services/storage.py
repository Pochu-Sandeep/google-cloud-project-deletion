class storage:

    def storage_list(self,project_id):

        from gcp_project_deletion.variable import storage_client

        storage_list = list(storage_client.list_buckets(project=project_id))

        if len(storage_list)>0:

            storage_exist = True

            for storage_name in storage_list:

                storage_deletion = storage_client.get_bucket(storage_name.name)

                storage_deletion.delete()

        else:

            storage_exist = False

        return storage_exist









