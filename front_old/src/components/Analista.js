import foto from '../assets/analista.png'

export default function Analista(props) {
    console.log(props)
    const analista = props.analista

    const deleteAnalista = () => {
        let url = 'http://127.0.0.1:5000/del_analista?id=' + analista.id;
        fetch(url, {
          method: 'delete'
        })
          .then((response) => response.json())
          .catch((error) => {
            console.error('Error:', error);
            
          });  
      }

    return (
        <article className="analista">
            <img src={foto} alt=""/>
            <h3 className="usuario">
                <span>{analista.usuario}</span>
            </h3>
            <p className="name-product">{analista.sobrenome}, {analista.nome}</p>
            <p className="name-product">{analista.email}</p>
            <button className="btn-delete" onClick={deleteAnalista}>Deletar</button>
        </article>
    );
}