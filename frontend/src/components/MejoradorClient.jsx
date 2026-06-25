import { useState } from "react";

// export default function MejoradorClient() {
export default function MejoradorClient({ action:propAction  }) {
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [result, setResult] = useState(null);
//   const [action, setAction] = useState("remove_bg");
  const [loading, setLoading] = useState(false);

  const action =
    propAction ??
    new URLSearchParams(window.location.search).get("action") ??
    "remove_bg";
// console.log({
//   action,
//   file,
// });
  const titles = {
  remove_bg: "Eliminar Fondo",
  grayscale: "Escala de Grises",
  edges: "Detección de Bordes",
  sepia: "Sepia",
  calidad: "Mejorar Calidad",
  blur: "Desenfocar",
};

const tools = {
    calidad: {
    title: "Mejorar Calidad",
    params: [],
  },
  remove_bg: {
    title: "Eliminar Fondo",
    params: [],
  },
  grayscale: {
    title: "Escala de Grises",
    params: [],
  },
  edges: {
    title: "Detección de Bordes",
    params: [
      { name: "threshold1", label: "Umbral 1", type: "range", min: 0, max: 255 },
      { name: "threshold2", label: "Umbral 2", type: "range", min: 0, max: 255 }
    ],
  },
  sepia: {
    title: "Sepia",
    params: [
      { name: "intensity", label: "Intensidad", type: "range", min: 0, max: 100 }
    ],
  },
  blur: {
    title: "Desenfocar",
    params: [
      { name: "blur", label: "Blur", type: "range", min: 1, max: 51 }
    ],
  },
};

const [params, setParams] = useState({});

  const handleFile = (f) => {
    if (!f) return;
    setFile(f);
    setPreview(URL.createObjectURL(f));
  };

  const sendImage = async () => {
    if (!file) return alert("Subí una imagen");

    const formData = new FormData();
    formData.append("image", file);
    formData.append("action", action || "remove_bg");
    formData.append("params", params ? JSON.stringify(params) : "{}");

    setLoading(true);

    const res = await fetch("http://127.0.0.1:5000/process", {
      method: "POST",
      body: formData,
    });

    const blob = await res.blob();
    setResult(URL.createObjectURL(blob));
    setLoading(false);
  };

  const download = () => {
    if (!result) return;

    const a = document.createElement("a");
    a.href = result;
    a.download = "resultado.png";
    a.click();
  };

  return (
    <div className="page">

    <h2 className="title">
      {tools[action]?.title}
    </h2>
      {/* DROPZONE */}
      <div
        className="dropzone"
        onDragOver={(e) => e.preventDefault()}
        onDrop={(e) => {
          e.preventDefault();
          handleFile(e.dataTransfer.files[0]);
        }}
      >
        {!preview ? (
          <p>📤 Arrastrá una imagen o hacé click</p>
        ) : (
          <img src={preview} />
        )
        }
        <input
          type="file"
          onChange={(e) => handleFile(e.target.files[0])}
        />

      </div>

      {/* CONTROLES */}
      <div className="panel">

         {/* PARAMETROS DINÁMICOS */}
        {tools[action]?.params.map((p) => (
            <div key={p.name} style={{ display: "flex", flexDirection: "column", gap: "4px" }}>
            <label>{p.label}</label>

            <input
                type={p.type}
                min={p.min}
                max={p.max}
                value={params[p.name] ?? p.min ?? 0}
                onChange={(e) =>
                    setParams({
                        ...params,
                        [p.name]: e.target.value,
                    })
                }
                />
            </div>
        ))}
        <button onClick={sendImage} disabled={loading}>
            {loading ? "Procesando..." : "Procesar"}
        </button>
        {result && (
          <button onClick={download}>
            Descargar resultado
          </button>
        )}
      </div>

      {/* COMPARACIÓN */}
      <div className="compare">
        {preview && (
          <div>
            <h4>Original</h4>
            <img src={preview} />
          </div>
        )}

        {result && (
          <div>
            <h4>Resultado</h4>
            <img src={result} />
          </div>
        )}
      </div>

    </div>
  );
}