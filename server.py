from fastapi import FastAPI, Request
import os
import json
app = FastAPI()


class repoManager:
    def __init__(self, repo_db:str):
        self.repo_db = repo_db
    
    def getRepoPath(self, id:str):
        with open(self.repo_db, "r") as repo_db:
            repo_db_dict = json.loads(repo_db.read())
            try:
                return repo_db_dict["repos"][id]
            except KeyError:
                return "No registery found"
        
repo_manager = repoManager("repo_db.json")

@app.get("/push")
def push(): 
    return {"operation": "push"}

@app.get("/pull")
def pull(id:str): 
    repoPath = repo_manager.getRepoPath(id)
    return {"operation": "pull", "path":repoPath}

@app.get("/")
def node():
    return {"message": "repoSync online ♻️"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)