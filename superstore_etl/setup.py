import os

# Disarankan menyimpan password ke environment variable di produksi
PWD = "SuperStore_Dicoding"
USER_ID = "postgres.tkzfqpuacgcimxkmeasq"  # Ganti sesuai credential Supabase kamu
SERVER = "aws-0-ap-southeast-1.pooler.supabase.com"  # Pooler Supabase
DB = "postgres"
DRIVER = "org.postgresql.Driver"

# Supabase pooler pakai port 6543
PORT = "6543"

# Source connection
src_url = f"jdbc:postgresql://{SERVER}:{PORT}/{DB}?user={USER_ID}&password={PWD}"

# Target connection (misalnya kamu ingin migrasi ke database kedua, ubah jika beda)
SERVER_TARGET = "aws-0-ap-southeast-1.pooler.supabase.com"  # Atau server target lainnya
target_url = f"jdbc:postgresql://{SERVER_TARGET}:{PORT}/{DB}?user={USER_ID}&password={PWD}"
