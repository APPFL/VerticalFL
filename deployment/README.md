# Deploying Vertical FL Using gRPC with APPFL

## How to Run?

You can start two terminals, one to run the server and one to run the three clients

```bash
python run_vfl_server.py
```

```bash
python run_vfl_client.py --config configs/client1.yaml &
python run_vfl_client.py --config configs/client2.yaml &
python run_vfl_client.py --config configs/client2.yaml &
```