# grpc_tutorial
сгенерировать клиентский и серверный интерфейсы gRPC из users/user.protoопределения службы. команда: 
python -m grpc_tools.protoc -I. --python_out=./grpc_codegen --grpc_python_out=./grpc_codegen ./users/user.proto
Запуск сервера  : python manage.py run_grpc_server
