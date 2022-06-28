import pandas as pd,ftplib,requests,os

df = pd.read_csv('')
path = 'C:/Users/.../chunk{}.csv'
file_size = df.memory_usage(index=True, deep=False).sum() / 1048576
print(file_size)


def save_file_part(df,size_threshold,save_path,part_number=0):
        file_size = df.memory_usage(index=True,deep=False).sum() / 1048576
        num_records = len(df)

        if file_size > size_threshold:
            records_to_split = int(num_records * size_threshold // file_size)
            df_to_keep = df.head(records_to_split)
            print(df_to_keep.memory_usage(index=True,deep=False).sum() / 1048576)
            df_to_keep.to_csv(save_path.format(part_number),index=False)
            save_file_part(df.tail(num_records-records_to_split), size_threshold,path,part_number=part_number+1)

        else:
            df.to_csv(save_path.format(part_number),index=False)


save_file_part(df,.3,path)



