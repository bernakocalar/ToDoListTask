import React from "react";
import type { Task } from "../types";

interface Props {
  tasks: Task[];
  title: string;
}

const TaskList: React.FC<Props> = ({ tasks }) => {
  return (
    <div>
      <h2 className="text-xl font-semibold mb-4">Görevler</h2>
      <ul>
        {tasks.map((task) => (
          <li key={task.name} className="border p-2 mb-2">
            <strong>{task.name}</strong> - {task.status ? "✅" : "⏳"}
            <p>{task.description}</p>
            <p>Bitiş: {task.deadline}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TaskList;
