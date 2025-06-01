import { useEffect, useState } from "react";
import Sidebar from "./components/Sidebar";
import TaskList from "./components/TaskList";
import type { Task, TaskListType } from "./types";
import axios from "axios";

function App() {
  const [lists, setLists] = useState<TaskListType[]>([]);
  const [selectedList, setSelectedList] = useState<TaskListType | null>(null);
  const [tasks, setTasks] = useState<Task[]>([]);

  useEffect(() => {
    // Tüm listeleri getir
    axios
      .get<TaskListType[]>("http://127.0.0.1:8000/lists")
      .then((response) => {
        setLists(response.data);
      })
      .catch((error) => {
        console.error("Listeler alınırken hata oluştu:", error);
      });
  }, []);

  useEffect(() => {
    // Seçilen listeye ait görevleri getir
    if (selectedList) {
      axios
        .get<Task[]>(`http://127.0.0.1:8000/lists/${selectedList.id}/items`)
        .then((response) => {
          setTasks(response.data);
        })
        .catch((error) => {
          console.error("Görevler alınırken hata oluştu:", error);
        });
    }
  }, [selectedList]);

  const handleSelectList = (listName: string) => {
    const found = lists.find((l) => l.name === listName);
    if (found) setSelectedList(found);
  };

  return (
    <div className="flex h-screen w-full">
      <Sidebar lists={lists.map((l) => l.name)} onSelect={handleSelectList} />
      <main className="w-3/4 p-4 overflow-y-auto">
        {selectedList ? (
          <TaskList title={selectedList.name} tasks={tasks} />
        ) : (
          <p>Liste seçiniz...</p>
        )}
      </main>
    </div>
  );
}

export default App;
