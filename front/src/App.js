import "./App.css";
import { useEffect, useState } from "react";
import axios from 'axios'
import {
  Button,
  EditableText,
  InputGroup,
  Toaster,
  Position,
} from "@blueprintjs/core";

const AppToaster = Toaster.create({
  position: Position.TOP,
});

function App() {

  const [users, setUsers] = useState([]);
  const [newNome, setNewNome] = useState("");
  const [newSobrenome, setNewSobrenome] = useState("");
  const [newUsuario, setNewUsuario] = useState("");
  const [newEmail, setNewEmail] = useState("");

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/get_analistas')
      .then(res => setUsers(res.data.analistas))
      .catch(error => console.log(error))
  }, []);

  const addUser = () => {
    const nome = newNome.trim();
    const sobrenome = newSobrenome.trim();
    const usuario = newUsuario.trim();
    const email = newEmail.trim();
    if (nome && sobrenome && usuario && email) {

      const formData = new FormData();
      formData.append("nome", nome);
      formData.append("sobrenome", sobrenome);
      formData.append("usuario", usuario);
      formData.append("email", email);

      fetch("http://127.0.0.1:5000/add_analista", {
        method: "POST",
        body: formData,
      })
        .then((response) => response.json())
        .then((data) => {
          setUsers([...users, data]);
          setNewNome("");
          setNewSobrenome("");
          setNewUsuario("");
          setNewEmail("");
          AppToaster.show({
            message: "Analista adicionado com sucesso!",
            intent: "success",
            timeout: 3000,
          });
        });
    }
  };

  const updateUser = (id) => {
    const user = users.find((user) => user.id === id);

    const formData = new FormData();
    formData.append("nome", user.nome);
    formData.append("sobrenome", user.sobrenome);
    formData.append("usuario", user.usuario);
    formData.append("email", user.email);

    fetch(`http://127.0.0.1:5000/put_analista?id=${id}`, {
      method: "PUT",
      body: formData,
    })
      .then((response) => response.json())
      .then(() => {
        AppToaster.show({
          message: "Analista atualizado com sucesso!",
          intent: "success",
          timeout: 3000,
        });
      });
  };

  const deleteUser = (id) => {
    fetch(`http://127.0.0.1:5000/del_analista?id=${id}`, {
      method: "DELETE",
    })
      .then((response) => response.json())
      .then(() => {
        setUsers((values) => {
          return values.filter((item) => item.id !== id);
        });
        AppToaster.show({
          message: "Analista deletado com sucesso!",
          intent: "success",
          timeout: 3000,
        });
      });
  };

  const onChangeHandler = (id, key, value) => {
    setUsers((values) => {
      return values.map((item) =>
        item.id === id ? { ...item, [key]: value } : item
      );
    });
  };

  return (
    <div className="App">
      <table class="bp4-html-table .modifier">
        <thead>
          <tr>
            <th>Id</th>
            <th>Nome</th>
            <th>Sobrenome</th>
            <th>Usuário</th>
            <th>Email</th>
          </tr>
        </thead>
        <tbody>
        <tr>
            <td></td>
            <td>
              <InputGroup
                placeholder="Nome"
                value={newNome}m
                onChange={(e) => setNewNome(e.target.value)}
              />
            </td>
            <td>
              <InputGroup
                placeholder="Sobrenome"
                value={newSobrenome}
                onChange={(e) => setNewSobrenome(e.target.value)}
              />
            </td>
            <td>
              <InputGroup
                placeholder="Usuário"
                value={newUsuario}
                onChange={(e) => setNewUsuario(e.target.value)}
              />
            </td>
            <td>
              <InputGroup
                placeholder="Email"
                value={newEmail}
                onChange={(e) => setNewEmail(e.target.value)}
              />
            </td>
            <td colSpan={2}>
              <Button intent="success" onClick={addUser}>
                Adiciona
              </Button>
            </td>
          </tr>
          {users.map((user) => (
            <tr key={user.id}>
              <td>{user.id}</td>
              <td>{user.nome}</td>
              <td>{user.sobrenome}</td>
              <td>
                <EditableText
                  value={user.usuario}
                  onChange={(value) => onChangeHandler(user.id, "usuario", value)}
                />
              </td>
              <td>
                <EditableText
                  value={user.email}
                  onChange={(value) => onChangeHandler(user.id, "email", value)
                  }
                />
              </td>
              <td>
                <Button intent="primary" onClick={() => updateUser(user.id)}>
                  Atualiza
                </Button>
                &nbsp;
                <Button intent="danger" onClick={() => deleteUser(user.id)}>
                  Deleta
                </Button>
              </td>
            </tr>
          ))}
        </tbody>
        <tfoot>

        </tfoot>
      </table>
    </div>
  );
}

export default App;
