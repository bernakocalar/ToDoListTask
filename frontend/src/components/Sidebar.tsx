import React from "react";

interface SidebarProps {
  lists: string[];
  onSelect: (listName: string) => void;
}

const Sidebar: React.FC<SidebarProps> = ({ lists, onSelect }) => {
  return (
    <aside className="w-2/4 bg-gray-100 p-4">
      <h2 className="text-xl font-bold mb-4">Listeler</h2>
      <ul>
        {lists.map((list, idx) => (
          <li
            key={idx}
            className="cursor-pointer hover:underline"
            onClick={() => onSelect(list)}
          >
            {list}
          </li>
        ))}
      </ul>
    </aside>
  );
};

export default Sidebar;
