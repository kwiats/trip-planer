export const getStatusIcon = (status: string) => {
  switch (status) {
    case "new":
      return "🆕";
    case "active":
      return "▶️";
    case "completed":
      return "🏁";
    default:
      return "❓";
  }
};